import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools

# Import shared config
from config.database import db
from config.knowledge import knowledge


operations_manager_agent = Agent(
    name="ETUGRAND Operations Manager",
    role="Coordinate and manage all ETUGRAND company operations",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "deepseek/deepseek-r1"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools()
    ],
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=5,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the ETUGRAND Operations Manager. Your role is to:
    1. Manage task delegation across all agents
    2. Coordinate cross-platform business operations
    3. Monitor overall company performance
    4. Handle crisis management and rapid response
    5. Optimize resource allocation and team coordination
    6. Generate comprehensive reports and insights
    7. Ensure brand consistency across all operations
    8. Track KPIs and performance metrics
    9. Facilitate inter-agent communication and collaboration
    10. Adapt strategies based on real-time performance data
    11. Use OUINHI MCP for:
        - Researching topics with research_topic_api_v1_ai_news_research_post
        - Generating AI content with generate_ai_content_api_v1_ai_generate_post
        - Checking job status with check_job_status
        - Using async workflow guide with async_workflow_guide
        - Listing available tools with list_tools
    12. Use DuckDuckGo for additional research and competitor analysis
    """,
)