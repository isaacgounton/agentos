import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

# Multi-server MCP configuration disabled due to missing external MCP servers
multi_mcp = None

research_agent = Agent(
    name="Research Analyst",
    role="Conduct market research and trend analysis",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "research_topic_api_v1_ai_news_research_post",
                "search_stock_videos_api_v1_ai_video_search_stock_videos_post",
                "search_stock_images_api_v1_ai_image_search_stock_images_post",
                "download_media_api_v1_media_download_post",
                "extract_metadata_api_v1_media_metadata_post",
                "convert_document_to_markdown_api_v1_documents_to_markdown_post",
                "check_job_status",
                "async_workflow_guide"
            ]
        ),
        DuckDuckGoTools()
    ] + ([multi_mcp] if multi_mcp else []),
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are a research analyst. Your role is to:
    1. Monitor trending topics and hashtags
    2. Analyze competitor content and strategies
    3. Identify content gaps and opportunities
    4. Track industry news and developments
    5. Generate content inspiration and ideas
    6. Research audience demographics and preferences
    7. Analyze social media trends and patterns
    8. Provide data-driven insights for content strategy
    9. Monitor brand mentions and sentiment
    10. Identify emerging platforms and technologies
    11. Use OUINHI MCP for:
        - Researching topics with research_topic_api_v1_ai_news_research_post
        - Searching stock videos with search_stock_videos_api_v1_ai_video_search_stock_videos_post
        - Searching stock images with search_stock_images_api_v1_ai_image_search_stock_images_post
        - Downloading media with download_media_api_v1_media_download_post
        - Extracting metadata with extract_metadata_api_v1_media_metadata_post
        - Converting documents to markdown with convert_document_to_markdown_api_v1_documents_to_markdown_post
        - Checking job status with check_job_status
        - Using async workflow guide with async_workflow_guide
    12. Use DuckDuckGo for additional research and web searches
    """,
)