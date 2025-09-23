import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools

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
    6. Use DuckDuckGo for researching trends and competitor analysis
    """,
)