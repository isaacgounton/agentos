import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

# Try to import additional file handling tools
try:
    import requests
    import aiofiles
    import mimetypes
    from pathlib import Path
    from typing import Optional, Dict, Any
    import json
    FILE_TOOLS_AVAILABLE = True
except ImportError:
    FILE_TOOLS_AVAILABLE = False

# Custom S3 tools for local file handling
class S3LocalTools:
    """Local file handling tools for S3 operations."""

    def __init__(self):
        self.download_cache = {}

    def download_file_from_url(self, url: str, save_path: Optional[str] = None) -> str:
        """
        Download a file from a URL and save it locally.

        Args:
            url: URL to download from
            save_path: Optional local path to save the file

        Returns:
            JSON string with download result
        """
        if not FILE_TOOLS_AVAILABLE:
            return json.dumps({"error": "File handling libraries not available"})

        try:
            # Download the file
            response = requests.get(url, stream=True)
            response.raise_for_status()

            # Determine filename and save path
            if not save_path:
                filename = url.split('/')[-1].split('?')[0] or 'downloaded_file'
                save_path = f"/tmp/{filename}"

            # Ensure directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Save the file
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Get file info
            file_size = os.path.getsize(save_path)
            mime_type, _ = mimetypes.guess_type(save_path)

            return json.dumps({
                "success": True,
                "file_path": save_path,
                "file_size": file_size,
                "mime_type": mime_type,
                "original_url": url,
                "message": f"File downloaded successfully to {save_path}"
            })

        except Exception as e:
            return json.dumps({"error": f"Download failed: {str(e)}"})

    def get_file_info(self, file_path: str) -> str:
        """
        Get information about a local file.

        Args:
            file_path: Path to the local file

        Returns:
            JSON string with file information
        """
        if not FILE_TOOLS_AVAILABLE:
            return json.dumps({"error": "File handling libraries not available"})

        try:
            if not os.path.exists(file_path):
                return json.dumps({"error": f"File not found: {file_path}"})

            file_stat = os.stat(file_path)
            mime_type, _ = mimetypes.guess_type(file_path)

            return json.dumps({
                "file_path": file_path,
                "file_size": file_stat.st_size,
                "mime_type": mime_type,
                "created_time": file_stat.st_ctime,
                "modified_time": file_stat.st_mtime,
                "is_readable": os.access(file_path, os.R_OK),
                "extension": Path(file_path).suffix.lower()
            })

        except Exception as e:
            return json.dumps({"error": f"Failed to get file info: {str(e)}"})

    def validate_file_for_upload(self, file_path: str, max_size_mb: int = 100) -> str:
        """
        Validate a file for S3 upload.

        Args:
            file_path: Path to the local file
            max_size_mb: Maximum file size in MB

        Returns:
            JSON string with validation result
        """
        if not FILE_TOOLS_AVAILABLE:
            return json.dumps({"error": "File handling libraries not available"})

        try:
            if not os.path.exists(file_path):
                return json.dumps({"error": f"File not found: {file_path}"})

            file_size = os.path.getsize(file_path)
            max_size_bytes = max_size_mb * 1024 * 1024

            if file_size > max_size_bytes:
                return json.dumps({
                    "valid": False,
                    "error": f"File too large: {file_size} bytes (max: {max_size_bytes} bytes)"
                })

            if not os.access(file_path, os.R_OK):
                return json.dumps({
                    "valid": False,
                    "error": f"File not readable: {file_path}"
                })

            mime_type, _ = mimetypes.guess_type(file_path)

            return json.dumps({
                "valid": True,
                "file_size": file_size,
                "mime_type": mime_type,
                "max_size_mb": max_size_mb,
                "message": "File is valid for upload"
            })

        except Exception as e:
            return json.dumps({"error": f"Validation failed: {str(e)}"})

s3_agent = Agent(
    name="S3 Manager",
    role="Manage S3 file uploads and downloads",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        S3LocalTools(),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "upload_file_api_v1_s3_upload_post",
                "async_workflow_guide"
            ]
        ),
    ],
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are an S3 file management specialist. Your role is to:

    CORE S3 OPERATIONS:
    1. Upload local files to S3 storage
    2. Download files from URLs and upload them to S3
    3. Manage file validation and error handling
    4. Support various file types and sizes
    5. Provide status updates and progress tracking
    6. Handle S3 credentials and configuration securely

    LOCAL FILE HANDLING (using S3LocalTools):
    7. Use download_file_from_url to:
       - Download files from any URL
       - Save files to temporary or specified locations
       - Handle large file downloads with streaming
       - Provide file size and MIME type information

    8. Use get_file_info to:
       - Get detailed file information
       - Check file existence and permissions
       - Determine file type and size
       - Validate file readiness for upload

    9. Use validate_file_for_upload to:
       - Check file size limits
       - Verify file readability
       - Detect MIME types
       - Ensure files meet S3 upload requirements

    S3 UPLOAD (using OUINHI MCP):
    10. Use upload_file_api_v1_s3_upload_post to:
        - Upload files to S3 storage
        - Handle authentication and permissions
        - Provide upload status and URLs
        - Manage upload errors and retries

    WORKFLOW EXAMPLES:
    11. URL to S3 workflow:
        - User provides URL
        - Download file using S3LocalTools.download_file_from_url
        - Validate downloaded file
        - Upload to S3 using OUINHI MCP tool
        - Return S3 URL and status

    12. Local file to S3 workflow:
        - User provides local file path
        - Validate file using S3LocalTools.validate_file_for_upload
        - Get file information
        - Upload to S3 using OUINHI MCP tool
        - Return S3 URL and status

    FILE TYPE SUPPORT:
    13. Handle common file types:
        - Images: JPG, PNG, GIF, SVG, WebP
        - Documents: PDF, DOC, DOCX, TXT, MD
        - Videos: MP4, AVI, MOV, WebM
        - Audio: MP3, WAV, OGG, AAC
        - Archives: ZIP, RAR, TAR, GZ

    ERROR HANDLING:
    14. Handle common issues:
        - Network timeouts and retries
        - File size limits
        - Unsupported file types
        - Permission errors
        - S3 upload failures
        - URL download failures

    BEST PRACTICES:
    15. Always validate files before upload
    16. Provide clear progress updates
    17. Handle large files efficiently
    18. Use appropriate error messages
    19. Maintain security for S3 credentials
    20. Support both local files and URL downloads

    Always use the most appropriate tools for each task and provide clear, actionable feedback about upload status and any issues encountered.
    """,
)