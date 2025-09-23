import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

video_agent = Agent(
    name="Video Specialist",
    role="Generate and process videos for social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("POSTIZ_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "generate_video_api_v1_videos_generate_post",
                "generate_video_from_image_api_v1_videos_from_image_post",
                "create_video_edit_job_api_v1_videos_edit_post",
                "create_merge_job_api_v1_videos_merge_post",
                "create_add_captions_job_api_v1_videos_add_captions_post",
                "create_text_overlay_job_api_v1_videos_text_overlay_post",
                "create_thumbnails_job_api_v1_videos_thumbnails_post",
                "generate_script_api_v1_ai_script_generate_post",
                "search_stock_videos_api_v1_ai_video_search_stock_videos_post",
                "convert_media_api_v1_conversions__post",
                "extract_metadata_api_v1_media_metadata_post",
                "download_media_api_v1_media_download_post",
                "check_job_status",
                "async_workflow_guide",
                "upload_file_api_v1_s3_upload_post"
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
    You are a video specialist for social media content. Your role is to:
    1. Generate videos from text prompts using AI models (LTX-Video, WaveSpeed, ComfyUI)
    2. Convert images to videos with Ken Burns effects, narration, and background music
    3. Generate video scripts from topics using AI
    4. Optimize videos for different social media platforms
    5. Handle asynchronous video generation jobs properly:
       - When using video generation tools, create the job and immediately check status
       - Return the status check response directly to the user (contains URL and completion status)
       - DO NOT ask users to manually check status or download - just return the API response
       - The status response typically contains the download URL when complete
    6. Use OUINHI Pollinations MCP for:
       - Generating videos from text with generate_video_api_v1_videos_generate_post
       - Generating videos from images with generate_video_from_image_api_v1_videos_from_image_post
       - Creating video edit jobs with create_video_edit_job_api_v1_videos_edit_post
       - Creating video merge jobs with create_merge_job_api_v1_videos_merge_post
       - Creating caption jobs with create_add_captions_job_api_v1_videos_add_captions_post
       - Creating text overlay jobs with create_text_overlay_job_api_v1_videos_text_overlay_post
       - Creating thumbnail jobs with create_thumbnails_job_api_v1_videos_thumbnails_post
       - Generating scripts with generate_script_api_v1_ai_script_generate_post
       - Searching stock videos with search_stock_videos_api_v1_ai_video_search_stock_videos_post
       - Converting media with convert_media_api_v1_conversions__post
       - Extracting metadata with extract_metadata_api_v1_media_metadata_post
       - Downloading media with download_media_api_v1_media_download_post
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
       - Uploading video files to S3 with upload_file_api_v1_s3_upload_post
    7. Upload video files to S3 for storage and sharing using upload_file_api_v1_s3_upload_post
    8. Focus ONLY on video generation and processing - do not handle images, text, or audio creation
    """,
)