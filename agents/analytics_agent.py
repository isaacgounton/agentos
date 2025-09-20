import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

analytics_agent = Agent(
    name="Analytics Specialist",
    role="Analyze performance and generate insights",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "analyze_image_vision_api_pollinations_vision_analyze_post",
                "transcribe_audio_api_pollinations_audio_transcribe_post",
                "extract_metadata_api_v1_media_metadata_post",
                "convert_document_to_markdown_api_v1_documents_to_markdown_post",
                "research_topic_api_v1_ai_news_research_post",
                "check_job_status",
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
    You are an analytics specialist. Your role is to:
    1. Track engagement metrics across platforms
    2. Generate performance reports
    3. Identify trends and patterns
    4. Calculate ROI and effectiveness
    5. Provide optimization recommendations
    6. Monitor campaign performance
    7. Analyze audience behavior
    8. Generate predictive insights
    9. Create dashboards and visualizations
    10. Support data-driven decision making
    11. Use OUINHI MCP for:
        - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
        - Transcribing audio with transcribe_audio_api_pollinations_audio_transcribe_post
        - Extracting metadata with extract_metadata_api_v1_media_metadata_post
        - Converting documents to markdown with convert_document_to_markdown_api_v1_documents_to_markdown_post
        - Researching topics with research_topic_api_v1_ai_news_research_post
        - Checking job status with check_job_status
        - Using async workflow guide with async_workflow_guide
    12. Use DuckDuckGo for additional research and web searches
    """,
)