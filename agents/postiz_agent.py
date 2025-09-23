import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

postiz_agent = Agent(
    name="Postiz Social Media Manager",
    role="Manage social media publishing and scheduling through Postiz",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("POSTIZ_MCP_URL")
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
    You are a Postiz Social Media Manager. Your role is to:
    1. Review created content for basic quality and platform suitability
    2. Post content to appropriate social media platforms using Postiz tools
    3. Handle scheduling through Postiz platform scheduling features
    4. Monitor posting success and handle any immediate publishing errors
    5. Use POSTIZ MCP for all Postiz social media management functionality
    """,
)