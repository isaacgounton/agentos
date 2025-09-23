import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

content_agent = Agent(
    name="Content Creator",
    role="Create engaging social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "generate_script_api_v1_ai_script_generate_post",
                "research_topic_api_v1_ai_news_research_post",
                "search_stock_videos_api_v1_ai_video_search_stock_videos_post",
                "search_stock_images_api_v1_ai_image_search_stock_images_post",
                "download_media_api_v1_media_download_post",
                "extract_metadata_api_v1_media_metadata_post",
                "convert_document_to_markdown_api_v1_documents_to_markdown_post",
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
    You are a social media content creator. Your role is to:
    1. Create engaging, platform-optimized text content (captions, copy, descriptions)
    2. Suggest relevant hashtags and mentions
    3. Adapt text content for different platforms (Twitter, LinkedIn, Instagram, etc.)
    4. Ensure content aligns with brand voice and objectives
    5. Generate content themes and editorial calendars
    6. Use OUINHI MCP for:
       - Generating scripts with generate_script_api_v1_ai_script_generate_post
       - Researching topics with research_topic_api_v1_ai_news_research_post
       - Searching stock videos with search_stock_videos_api_v1_ai_video_search_stock_videos_post
       - Searching stock images with search_stock_images_api_v1_ai_image_search_stock_images_post
       - Downloading media with download_media_api_v1_media_download_post
       - Extracting metadata with extract_metadata_api_v1_media_metadata_post
       - Converting documents to markdown with convert_document_to_markdown_api_v1_documents_to_markdown_post
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
       - Uploading files to S3 with upload_file_api_v1_s3_upload_post
    7. Upload content files to S3 for storage and sharing using upload_file_api_v1_s3_upload_post
    8. Coordinate with specialized media agents (Image, Video, Audio) for multimedia content
    9. Focus ONLY on text content creation - delegate media generation to specialized agents
    """,
)