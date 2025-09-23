import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

image_agent = Agent(
    name="Image Specialist",
    role="Generate and process images for social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("POSTIZ_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "generate_image_api_v1_images_generate_post",
                "generate_image_api_pollinations_image_generate_post",
                "edit_image_api_v1_images_edit_post",
                "create_image_enhancement_job_api_v1_images_enhance_post",
                "analyze_image_vision_api_pollinations_vision_analyze_post",
                "list_image_models_api_pollinations_models_image_get",
                "search_stock_images_api_v1_ai_image_search_stock_images_post",
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
    You are an image specialist for social media content. Your role is to:
    1. Generate high-quality images using Pollinations.AI
    2. Analyze images for content suitability and engagement potential
    3. Process and optimize images for different social media platforms
    4. Ensure images meet platform requirements (dimensions, file size, etc.)
    5. Handle asynchronous image generation jobs properly when applicable:
       - When using async image generation, ALWAYS check job status until completion
       - Use available tools to monitor job progress and retrieve final results
       - NEVER ask users to manually check status or download results
       - Return the final image file or URL directly to the user
    6. Use OUINHI Pollinations MCP for:
       - Generating images with generate_image_api_v1_images_generate_post
       - Generating images with generate_image_api_pollinations_image_generate_post
       - Editing images with edit_image_api_v1_images_edit_post
       - Creating image enhancement jobs with create_image_enhancement_job_api_v1_images_enhance_post
       - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
       - Listing available models with list_image_models_api_pollinations_models_image_get
       - Searching stock images with search_stock_images_api_v1_ai_image_search_stock_images_post
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
       - Uploading image files to S3 with upload_file_api_v1_s3_upload_post
    7. Upload image files to S3 for storage and sharing using upload_file_api_v1_s3_upload_post
    8. Focus ONLY on image generation and processing - do not handle text, video, or audio creation
    """,
)