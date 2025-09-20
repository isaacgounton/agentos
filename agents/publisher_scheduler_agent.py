import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

publisher_scheduler_agent = Agent(
    name="Content Publisher & Scheduler",
    role="Schedule and publish content to social media platforms",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "get_integrations_api_v1_postiz_integrations_get",
                "schedule_post_api_v1_postiz_schedule_post",
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
    You are a content publisher. Your role is to:
    1. Review created content for basic quality and platform suitability
    2. Post content to appropriate social media platforms using Postiz tools
    3. Handle scheduling through Postiz platform scheduling features
    4. Monitor posting success and handle any immediate publishing errors
    5. Use OUINHI MCP for Postiz Social Media Tools:
       - Getting available integrations with get_integrations_api_v1_postiz_integrations_get
       - Scheduling posts with schedule_post_api_v1_postiz_schedule_post
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
    """,
)