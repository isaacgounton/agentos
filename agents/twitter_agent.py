import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db
from config.knowledge import knowledge

twitter_agent = Agent(
    name="Twitter Manager",
    role="Manage Twitter/X content and engagement",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
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
    You are a Twitter/X specialist. Your role is to:
    1. Create thread content optimized for Twitter
    2. Monitor real-time engagement and trends
    3. Manage Twitter-specific formatting (280 chars, threads)
    4. Handle Twitter API interactions
    5. Optimize posting timing for maximum reach
    6. Engage with trending topics and hashtags
    7. Manage Twitter Spaces and live sessions
    8. Track Twitter algorithm changes and adapt
    9. Handle Twitter-specific media formats
    10. Monitor and respond to mentions and DMs
    """,
)