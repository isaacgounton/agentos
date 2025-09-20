import os
from agno.workflow.workflow import Workflow
from agno.workflow.step import Step

# Import shared config
from config.database import db

# Import agents
from agents.analytics_agent import analytics_agent
from agents.operations_manager_agent import operations_manager_agent

crisis_workflow = Workflow(
    name="Crisis Management Workflow",
    description="Handle business crises and operational challenges",
    db=db,
    steps=[
        Step(
            name="detect_crisis",
            description="Detect and assess crisis situation",
            agent=analytics_agent,
        ),
        Step(
            name="develop_response",
            description="Develop crisis response strategy",
            agent=operations_manager_agent,
        ),
        Step(
            name="coordinate_response",
            description="Coordinate response across all platforms",
            agent=operations_manager_agent,
        ),
        Step(
            name="monitor_recovery",
            description="Monitor situation and recovery progress",
            agent=analytics_agent,
        ),
    ],
)