from agno.workflow.workflow import Workflow
from agno.workflow.step import Step

# Import shared config
from config.database import db

# Import agents
from agents.research_agent import research_agent
from agents.content_agent import content_agent
from agents.operations_manager_agent import operations_manager_agent
from agents.postiz_agent import postiz_agent as publisher_scheduler_agent
from agents.analytics_agent import analytics_agent

daily_operations_workflow = Workflow(
    name="Daily Operations Workflow",
    description="Daily business operations and content management",
    db=db,
    steps=[
        Step(
            name="research_trends",
            description="Research trending topics and audience interests",
            agent=research_agent,
        ),
        Step(
            name="create_content",
            description="Generate content for all platforms",
            agent=content_agent,
        ),
        Step(
            name="optimize_platform",
            description="Optimize content for each platform",
            agent=operations_manager_agent,
        ),
        Step(
            name="schedule_publish",
            description="Schedule and publish optimized content",
            agent=publisher_scheduler_agent,
        ),
        Step(
            name="analyze_performance",
            description="Analyze content performance and engagement",
            agent=analytics_agent,
        ),
    ],
)