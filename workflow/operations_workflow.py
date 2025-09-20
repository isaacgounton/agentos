import os
from agno.workflow.workflow import Workflow
from agno.workflow.step import Step

# Import shared config
from config.database import db

# Import agents
from agents.engagement_agent import engagement_agent
from agents.content_agent import content_agent
from agents.image_agent import image_agent
from agents.video_agent import video_agent
from agents.audio_agent import audio_agent
from agents.publisher_scheduler_agent import publisher_scheduler_agent

operations_workflow = Workflow(
    id="operations-workflow",
    name="ETUGRAND Operations Workflow",
    description="End-to-end business operations and content management workflow",
    db=db,
    steps=[
        Step(
            name="research_topic",
            description="Research trending topics and audience interests",
            agent=engagement_agent,
        ),
        Step(
            name="create_text_content",
            description="Create engaging text content, captions, and scripts",
            agent=content_agent,
        ),
        Step(
            name="generate_images",
            description="Generate images for the content using AI",
            agent=image_agent,
        ),
        Step(
            name="generate_videos",
            description="Generate videos for the content using AI",
            agent=video_agent,
        ),
        Step(
            name="generate_audio",
            description="Generate audio for the content using TTS",
            agent=audio_agent,
        ),
        Step(
            name="publish_content",
            description="Publish the created content to social media platforms",
            agent=publisher_scheduler_agent,
        ),
    ],
)