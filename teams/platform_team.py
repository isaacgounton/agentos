import os
from agno.team import Team
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db

# Import agents
from ..agents.twitter_agent import twitter_agent
from ..agents.linkedin_agent import linkedin_agent
from ..agents.youtube_platform_agent import youtube_agent
from ..agents.reddit_agent import reddit_agent

platform_team = Team(
    name="Platform Management Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[twitter_agent, linkedin_agent, youtube_agent, reddit_agent],
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the Platform Management Team. Work together to:
    1. Manage platform-specific content and engagement
    2. Coordinate cross-platform campaigns
    3. Optimize posting strategies per platform
    4. Handle platform-specific challenges
    5. Share best practices across platforms
    6. Monitor platform algorithm changes
    7. Adapt content for platform requirements
    8. Track platform-specific performance metrics
    """,
)