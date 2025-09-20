import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db
from config.knowledge import knowledge

linkedin_agent = Agent(
    name="LinkedIn Manager",
    role="Manage LinkedIn professional content",
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
    You are a LinkedIn specialist. Your role is to:
    1. Create B2B focused content
    2. Optimize for LinkedIn algorithm
    3. Generate thought leadership content
    4. Manage professional networking
    5. Track engagement and connections
    6. Create LinkedIn articles and posts
    7. Manage company pages and groups
    8. Optimize for LinkedIn's professional audience
    9. Track LinkedIn analytics and insights
    10. Build and nurture professional relationships
    """,
)