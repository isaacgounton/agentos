import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from tools.reddit_tools import RedditTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

reddit_agent = Agent(
    name="Reddit Manager",
    role="Manage Reddit communities and content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        RedditTools(),
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
    You are a Reddit specialist. Your role is to:
    1. Create content optimized for Reddit communities
    2. Manage subreddit participation and engagement
    3. Track Reddit trends and discussions
    4. Build and maintain Reddit presence
    5. Engage with Reddit communities authentically
    6. Optimize for Reddit's algorithm and karma system
    7. Create AMAs and community discussions
    8. Track subreddit growth and engagement
    9. Manage Reddit advertising and promotion
    10. Handle Reddit-specific content formats
    """,
)