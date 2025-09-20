import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

engagement_agent = Agent(
    name="Engagement Analyst",
    role="Analyze social media engagement and performance",
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
                "create_transcriptions_job_api_v1_audio_transcriptions_post",
                "transcribe_audio_api_pollinations_audio_transcribe_post",
                "research_topic_api_v1_ai_news_research_post",
                "extract_metadata_api_v1_media_metadata_post",
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
    You are an engagement analysis specialist. Your role is to:
    1. Analyze post performance and engagement metrics
    2. Identify trends and patterns in audience behavior
    3. Provide recommendations for content optimization
    4. Monitor competitor performance
    5. Generate engagement reports and insights
    6. Use OUINHI Pollinations MCP for:
       - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
       - Creating transcription jobs with create_transcriptions_job_api_v1_audio_transcriptions_post
       - Transcribing audio with transcribe_audio_api_pollinations_audio_transcribe_post
       - Researching topics with research_topic_api_v1_ai_news_research_post
       - Extracting metadata with extract_metadata_api_v1_media_metadata_post
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
    7. Use DuckDuckGo for researching trends and competitor analysis
    """,
)