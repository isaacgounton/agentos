"""
Social Media AgentOS - Proper implementation following AgentOS patterns
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.knowledge.knowledge import Knowledge
from agno.models.openrouter import OpenRouter
from agno.os import AgentOS
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools
from agno.vectordb.pgvector import PgVector
from agno.workflow.workflow import Workflow
from agno.workflow.step import Step

# Database setup
db_url = os.getenv("DATABASE_URL", "postgresql+psycopg://ai:ai@localhost:5532/ai")
db = PostgresDb(db_url=db_url)

# Vector database for knowledge (using OpenAI for embeddings)
vector_db = PgVector(
    db_url=db_url,
    table_name="social_media_knowledge",
)

# Knowledge base for social media content and strategies
knowledge = Knowledge(
    name="Social Media Knowledge",
    contents_db=db,
    vector_db=vector_db,
)

# Content creation agent
content_agent = Agent(
    name="Content Creator",
    role="Create engaging social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are a social media content creator. Your role is to:
    1. Create engaging, platform-optimized text content (captions, copy, descriptions)
    2. Suggest relevant hashtags and mentions
    3. Adapt text content for different platforms (Twitter, LinkedIn, Instagram, etc.)
    4. Ensure content aligns with brand voice and objectives
    5. Generate content themes and editorial calendars
    6. Use OUINHI MCP for:
       - Creating text content with generate_text_api_pollinations_text_generate_post
       - Creating chat completions with create_chat_completion_api_pollinations_chat_completions_post
       - Generating scripts with generate_script_api_v1_ai_script_generate_post
    7. Coordinate with specialized media agents (Image, Video, Audio) for multimedia content
    8. Focus ONLY on text content creation - delegate media generation to specialized agents
    """,
)

# Engagement analysis agent
engagement_agent = Agent(
    name="Engagement Analyst",
    role="Analyze social media engagement and performance",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are an engagement analysis specialist. Your role is to:
    1. Analyze post performance and engagement metrics
    2. Identify trends and patterns in audience behavior
    3. Provide recommendations for content optimization
    4. Monitor competitor performance
    5. Generate engagement reports and insights
    6. Use OUINHI Pollinations MCP for:
       - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
       - Analyzing uploaded images with analyze_uploaded_image_api_pollinations_vision_analyze_upload_post
       - Transcribing audio content with transcribe_audio_api_pollinations_audio_transcribe_post
    7. Use DuckDuckGo for researching trends and competitor analysis
    """,
)

# Content publisher & scheduler agent
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
                "schedule_job_post_api_v1_postiz_schedule_job_post",
                "schedule_post_now_api_v1_postiz_schedule_now_post",
                "create_draft_post_api_v1_postiz_create_draft_post"
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
       - Scheduling posts from jobs with schedule_job_post_api_v1_postiz_schedule_job_post
       - Posting immediately with schedule_post_now_api_v1_postiz_schedule_now_post
       - Posting as draft posts with create_draft_post_api_v1_postiz_create_draft_post
    """,
)

# Image generation agent
image_agent = Agent(
    name="Image Specialist",
    role="Generate and process images for social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are an image specialist for social media content. Your role is to:
    1. Generate high-quality images using Pollinations.AI
    2. Analyze images for content suitability and engagement potential
    3. Process and optimize images for different social media platforms
    4. Ensure images meet platform requirements (dimensions, file size, etc.)
    5. Handle asynchronous image generation jobs properly when applicable:
       - When using async image generation, ALWAYS check job status until completion
       - Use available tools to monitor job progress and retrieve final results
       - NEVER ask users to manually check status or download results
       - Return the final image file or URL directly to the user
    6. Use OUINHI Pollinations MCP for:
       - Generating images with generate_image_api_pollinations_image_generate_post
       - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
       - Analyzing uploaded images with analyze_uploaded_image_api_pollinations_vision_analyze_upload_post
       - Listing available models with list_image_models_api_pollinations_models_image_get
    7. Focus ONLY on image generation and processing - do not handle text, video, or audio creation
    """,
)

# Video generation agent
video_agent = Agent(
    name="Video Specialist",
    role="Generate and process videos for social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are a video specialist for social media content. Your role is to:
    1. Generate videos from text prompts using AI models (LTX-Video, WaveSpeed, ComfyUI)
    2. Convert images to videos with Ken Burns effects, narration, and background music
    3. Generate video scripts from topics using AI
    4. Optimize videos for different social media platforms
    5. Handle asynchronous video generation jobs properly:
       - When using create_video_generation_job_api_v1_videos_generations_post, create the job and immediately check status
       - Return the status check response directly to the user (contains URL and completion status)
       - DO NOT ask users to manually check status or download - just return the API response
       - The status response typically contains the download URL when complete
    6. Use OUINHI Pollinations MCP for:
       - Creating video generation jobs with create_video_generation_job_api_v1_videos_generations_post
       - Checking job status with get_video_job_status_api_v1_videos_{job_id}_get
       - Generating videos from text with generate_video_api_v1_videos_generate_post
       - Generating scripts with generate_script_api_v1_ai_script_generate_post
    7. Focus ONLY on video generation and processing - do not handle images, text, or audio creation
    """,
)

# Audio generation agent
audio_agent = Agent(
    name="Audio Specialist",
    role="Generate and process audio for social media content",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are an audio specialist for social media content. Your role is to:
    1. Convert text to speech using various TTS engines (Kokoro, Piper, Edge TTS)
    2. Generate speech audio from text using Pollinations TTS
    3. Transcribe audio files for content analysis
    4. Optimize audio for different social media platforms
    5. Handle asynchronous audio generation jobs properly:
       - When using create_speech_job_api_v1_audio_speech_post, create the job and immediately check status
       - Return the status check response directly to the user (contains URL and completion status)
       - DO NOT ask users to manually check status or download - just return the API response
       - The status response typically contains the download URL when complete
    6. Use OUINHI Pollinations MCP for:
       - Creating speech jobs with create_speech_job_api_v1_audio_speech_post
       - Checking job status with get_speech_job_status_api_v1_audio_speech_{job_id}_get
       - Text-to-speech with text_to_speech_api_pollinations_audio_tts_post
       - Transcribing audio with transcribe_audio_api_pollinations_audio_transcribe_post
       - Listing voices with list_available_voices_api_pollinations_voices_get
    7. Focus ONLY on audio generation and processing - do not handle images, videos, or text creation
    """,
)

# Multi-server MCP configuration disabled due to missing external MCP servers
multi_mcp = None

# Social Media Manager Agent (2.2)
social_media_manager_agent = Agent(
    name="Social Media Manager",
    role="Coordinate and manage all social media operations",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
        ),
        DuckDuckGoTools()
    ] + ([multi_mcp] if multi_mcp else []),
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=5,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the Social Media Manager. Your role is to:
    1. Manage task delegation across all agents
    2. Coordinate cross-platform content strategies
    3. Monitor overall social media performance
    4. Handle crisis management and rapid response
    5. Optimize resource allocation and team coordination
    6. Generate comprehensive reports and insights
    7. Ensure brand consistency across all platforms
    8. Track KPIs and performance metrics
    9. Facilitate inter-agent communication and collaboration
    10. Adapt strategies based on real-time performance data
    """,
)

# Research Agent (2.4)
research_agent = Agent(
    name="Research Analyst",
    role="Conduct market research and trend analysis",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
        ),
        DuckDuckGoTools()
    ] + ([multi_mcp] if multi_mcp else []),
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are a research analyst. Your role is to:
    1. Monitor trending topics and hashtags
    2. Analyze competitor content and strategies
    3. Identify content gaps and opportunities
    4. Track industry news and developments
    5. Generate content inspiration and ideas
    6. Research audience demographics and preferences
    7. Analyze social media trends and patterns
    8. Provide data-driven insights for content strategy
    9. Monitor brand mentions and sentiment
    10. Identify emerging platforms and technologies
    """,
)

# Analytics Agent (2.6)
analytics_agent = Agent(
    name="Analytics Specialist",
    role="Analyze performance and generate insights",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp")
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
    You are an analytics specialist. Your role is to:
    1. Track engagement metrics across platforms
    2. Generate performance reports
    3. Identify trends and patterns
    4. Calculate ROI and effectiveness
    5. Provide optimization recommendations
    6. Monitor campaign performance
    7. Analyze audience behavior
    8. Generate predictive insights
    9. Create dashboards and visualizations
    10. Support data-driven decision making
    """,
)

# Platform-Specific Agents (2.5)

# Twitter Agent
twitter_agent = Agent(
    name="Twitter Manager",
    role="Manage Twitter/X content and engagement",
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
    You are a Twitter/X specialist. Your role is to:
    1. Create thread content optimized for Twitter
    2. Monitor real-time engagement and trends
    3. Manage Twitter-specific formatting (280 chars, threads)
    4. Handle Twitter API interactions
    5. Optimize posting timing for maximum reach
    6. Engage with trending topics and hashtags
    7. Manage Twitter Spaces and live sessions
    8. Track Twitter algorithm changes and adapt
    9. Handle Twitter-specific media formats
    10. Monitor and respond to mentions and DMs
    """,
)

# LinkedIn Agent
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

# YouTube Agent
youtube_agent = Agent(
    name="YouTube Manager",
    role="Manage YouTube content and channel growth",
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
    You are a YouTube specialist. Your role is to:
    1. Create video content optimized for YouTube algorithm
    2. Optimize titles, descriptions, and thumbnails
    3. Manage YouTube SEO and discoverability
    4. Track video performance and analytics
    5. Create video series and playlists
    6. Engage with YouTube community and comments
    7. Optimize for YouTube's recommendation system
    8. Manage video production workflow
    9. Track YouTube trends and viral content
    10. Build and maintain YouTube channel presence
    """,
)

# Reddit Agent
reddit_agent = Agent(
    name="Reddit Manager",
    role="Manage Reddit communities and content",
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
    You are a Reddit specialist. Your role is to:
    1. Create content optimized for Reddit communities
    2. Manage subreddit participation and engagement
    3. Track Reddit trends and discussions
    4. Build and maintain Reddit presence
    5. Engage with Reddit communities authentically
    6. Optimize for Reddit's algorithm and karma system
    7. Create AMAs and community discussions
    8. Track subreddit growth and engagement
    9. Manage Reddit advertising and promotion
    10. Handle Reddit-specific content formats
    """,
)

# Social media team
social_media_team = Team(
    id="social-media-team",
    name="Social Media Management Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[content_agent, engagement_agent, image_agent, video_agent, audio_agent, publisher_scheduler_agent],
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are a social media management team. Work together to:
    1. Create comprehensive social media strategies
    2. Coordinate content creation, media generation, scheduling, and publishing workflows
    3. Analyze performance and optimize campaigns
    4. Provide actionable insights for growth
    5. Leverage specialized tools across team members:
       - Content Creator: OUINHI MCP for text content and script generation
       - Image Specialist: OUINHI MCP for image generation and analysis
       - Video Specialist: OUINHI MCP for video generation and processing
       - Audio Specialist: OUINHI MCP for audio generation and transcription
       - Engagement Analyst: DuckDuckGo + OUINHI MCP for research and analysis
       - Publisher: Postiz tools for social media platform publishing
    6. Ensure clear separation of responsibilities between specialized agents
    """,
)

# Platform Management Team (3.3)
platform_team = Team(
    name="Platform Management Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[twitter_agent, linkedin_agent, youtube_agent, reddit_agent],
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are the Platform Management Team. Work together to:
    1. Manage platform-specific content and engagement
    2. Coordinate cross-platform campaigns
    3. Optimize posting strategies per platform
    4. Handle platform-specific challenges
    5. Share best practices across platforms
    6. Monitor platform algorithm changes
    7. Adapt content for platform requirements
    8. Track platform-specific performance metrics
    """,
)

# Strategy Team (3.4)
strategy_team = Team(
    name="Strategy Team",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    db=db,
    members=[social_media_manager_agent, analytics_agent, research_agent],
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

# Content creation workflow
content_workflow = Workflow(
    id="content-creation-workflow",
    name="Content Creation Workflow",
    description="End-to-end content creation and publishing workflow",
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

# Daily Content Creation Workflow (4.2)
daily_content_workflow = Workflow(
    name="Daily Content Creation Workflow",
    description="Create and publish daily social media content",
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
            agent=social_media_manager_agent,
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

# Crisis Management Workflow (4.3)
crisis_workflow = Workflow(
    name="Crisis Management Workflow",
    description="Handle social media crises and negative situations",
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
            agent=social_media_manager_agent,
        ),
        Step(
            name="coordinate_response",
            description="Coordinate response across all platforms",
            agent=social_media_manager_agent,
        ),
        Step(
            name="monitor_recovery",
            description="Monitor situation and recovery progress",
            agent=analytics_agent,
        ),
    ],
)

# Campaign Workflow (4.4)
campaign_workflow = Workflow(
    name="Social Media Campaign Workflow",
    description="Manage end-to-end social media campaigns",
    db=db,
    steps=[
        Step(
            name="campaign_planning",
            description="Plan campaign strategy and goals",
            agent=social_media_manager_agent,
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
            agent=social_media_manager_agent,
        ),
    ],
)

# Main AgentOS application
agent_os = AgentOS(
    os_id="social-media-agentos",
    description="Social Media AgentOS - AI-powered social media management platform",
    agents=[
        content_agent,
        engagement_agent,
        image_agent,
        video_agent,
        audio_agent,
        publisher_scheduler_agent,
        social_media_manager_agent,
        research_agent,
        analytics_agent,
        twitter_agent,
        linkedin_agent,
        youtube_agent,
        reddit_agent
    ],
    teams=[social_media_team, platform_team, strategy_team],
    workflows=[content_workflow, daily_content_workflow, crisis_workflow, campaign_workflow],
)

# Get the FastAPI app
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="social_media_agentos:app", port=7777)