from agno.workflow.workflow import Workflow
from agno.workflow.step import Step

# Import shared config
from config.database import db

# Import agents
from agents.operations_manager_agent import operations_manager_agent
from agents.content_agent import content_agent
from agents.postiz_agent import postiz_agent as publisher_scheduler_agent
from agents.analytics_agent import analytics_agent

campaign_workflow = Workflow(
    name="Business Campaign Workflow",
    description="Manage end-to-end business operations campaigns",
    db=db,
    steps=[
        Step(
            name="campaign_planning",
            description="Plan campaign strategy and goals",
            agent=operations_manager_agent,
        ),
        Step(
            name="content_development",
            description="Develop campaign content and assets",
            agent=content_agent,
        ),
        Step(
            name="platform_execution",
            description="Execute campaign across platforms",
            agent=publisher_scheduler_agent,
        ),
        Step(
            name="performance_monitoring",
            description="Monitor campaign performance",
            agent=analytics_agent,
        ),
        Step(
            name="optimization_adjustments",
            description="Make optimization adjustments",
            agent=operations_manager_agent,
        ),
    ],
)