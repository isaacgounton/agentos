import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

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
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "create_speech_job_api_v1_audio_speech_post",
                "transcribe_audio_api_pollinations_audio_transcribe_post",
                "get_voices_formatted_api_v1_audio_voices_formatted_get",
                "get_models_formatted_api_v1_audio_models_formatted_get",
                "get_supported_providers_api_v1_audio_providers_get",
                "check_job_status",
                "async_workflow_guide",
                "upload_file_api_v1_s3_upload_post"
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
       - Transcribing audio with transcribe_audio_api_pollinations_audio_transcribe_post
       - Getting formatted voices with get_voices_formatted_api_v1_audio_voices_formatted_get
       - Getting formatted models with get_models_formatted_api_v1_audio_models_formatted_get
       - Getting supported providers with get_supported_providers_api_v1_audio_providers_get
       - Checking job status with check_job_status
       - Using async workflow guide with async_workflow_guide
       - Uploading audio files to S3 with upload_file_api_v1_s3_upload_post
    7. Upload audio files to S3 for storage and sharing using upload_file_api_v1_s3_upload_post
    8. Focus ONLY on audio generation and processing - do not handle images, videos, or text creation
    """,
)