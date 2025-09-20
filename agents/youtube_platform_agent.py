import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db
from config.knowledge import knowledge

youtube_agent = Agent(
    name="YouTube Manager",
    role="Manage YouTube content and channel growth",
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
    You are a YouTube specialist. Your role is to:
    1. Create video content optimized for YouTube algorithm
    2. Optimize titles, descriptions, and thumbnails
    3. Manage YouTube SEO and discoverability
    4. Track video performance and analytics
    5. Create video series and playlists
    6. Engage with YouTube community and comments
    7. Optimize for YouTube's recommendation system
    8. Manage video production workflow
    9. Track YouTube trends and viral content
    10. Build and maintain YouTube channel presence
    """,
)