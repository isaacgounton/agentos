import os
from agno.team import Team
from agno.models.openrouter import OpenRouter

# Import shared config
from config.database import db

# Import agents
from agents.operations_manager_agent import operations_manager_agent
from agents.analytics_agent import analytics_agent
from agents.research_agent import research_agent

strategy_team = Team(
    name="Strategy Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[operations_manager_agent, analytics_agent, research_agent],
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the Strategy Team. Work together to:
    1. Develop and oversee social media strategy
    2. Analyze performance and provide insights
    3. Optimize overall social media operations
    4. Generate strategic recommendations
    5. Monitor market trends and competition
    6. Plan long-term content and growth strategies
    7. Coordinate with platform teams for execution
    8. Provide data-driven strategic guidance
    """,
)