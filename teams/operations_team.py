import os
from agno.team import Team
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db

# Import agents
from agents.content_agent import content_agent
from agents.engagement_agent import engagement_agent
from agents.image_agent import image_agent
from agents.video_agent import video_agent
from agents.audio_agent import audio_agent
from agents.postiz_agent import postiz_agent

operations_team = Team(
    id="operations-team",
    name="ETUGRAND Operations Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[content_agent, engagement_agent, image_agent, video_agent, audio_agent, postiz_agent],
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the ETUGRAND Operations Team. Work together to:
    1. Create comprehensive business operations strategies
    2. Coordinate content creation, media generation, scheduling, and publishing workflows
    3. Analyze performance and optimize operations
    4. Provide actionable insights for business growth
    5. Leverage specialized tools across team members:
       - Content Creator: OUINHI MCP for text content and script generation
       - Image Specialist: OUINHI MCP for image generation and analysis
       - Video Specialist: OUINHI MCP for video generation and processing
       - Audio Specialist: OUINHI MCP for audio generation and transcription
       - Engagement Analyst: DuckDuckGo + OUINHI MCP for research and analysis
       - Publisher: Postiz tools for social media platform publishing
    6. Ensure clear separation of responsibilities between specialized agents
    """,
)