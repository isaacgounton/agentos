Project Setup (Section 1): Create the directory structure and environment
Database Setup (Section 1.2): Configure PostgreSQL and PgVector
Core Agents (Section 2): Implement the base agent class and orchestrator
MCP Integration (Section 7): Set up the MCP servers and connections

we will use
OPENROUTER_API_KEY and OPENROUTER_MODEL_NAME as llm provider
openai for embedding
pollinations mcp for images, vision , and andio, video

Pollinations
We can use <https://mcp.sequa.ai/v1/pollinations/contribute>>

or

{
  "mcpServers": {
    "pollinations": {
      "command": "npx",
      "args": [
        "@pollinations/model-context-protocol"
      ]
    }
  }
}
Run with npx (no installation required)
npx @pollinations/model-context-protocol

## Pollinations.AI Tools from ouinhi-mcp

### Image Generation & Analysis

- __generate_image_api_pollinations_image_generate_post__ - Generate images using Pollinations.AI
- __analyze_image_vision_api_pollinations_vision_analyze_post__ - Analyze images using Pollinations Vision API
- __analyze_uploaded_image_api_pollinations_vision_analyze_upload_post__ - Analyze uploaded image files
- __list_image_models_api_pollinations_models_image_get__ - List available Pollinations image generation models

### Text & Chat

- __list_text_models_api_pollinations_models_text_get__ - List available Pollinations text/vision models and voices
- __generate_text_api_pollinations_text_generate_post__ - Generate text using Pollinations.AI Text API
- __create_chat_completion_api_pollinations_chat_completions_post__ - Create chat completions with advanced features like vision and function calling

### Audio Processing

- __text_to_speech_api_pollinations_audio_tts_post__ - Generate speech audio from text
- __transcribe_audio_api_pollinations_audio_transcribe_post__ - Transcribe audio files using Pollinations STT
- __list_available_voices_api_pollinations_voices_get__ - List available TTS voices for audio generation

These tools provide comprehensive access to Pollinations.AI's capabilities for AI-powered image generation, text generation, vision analysis, and audio processing through the ouinhi-mcp server.

The tool to check job status and get the response is:

## __check_job_status__

- __Purpose__: Check the status of an asynchronous job by its ID
- __Description__: Essential for monitoring async operations like video generation, image processing, audio conversion, etc. Most API operations return a job ID immediately, and you must use this tool to check when the job is complete and get the final result.

__Parameters:__

- `job_id`: The job ID returned from an async operation (string)

__Returns:__

- Job status information including progress, completion status, and final result when ready

__Usage Pattern:__

1. Call an async operation (generation, processing, etc.) - it returns a job ID
2. Use this tool to check status periodically until job is complete
3. Once status shows 'completed', the result will be available in the response

This is the primary tool you'll use to monitor and retrieve results from any asynchronous operations in the ouinhi-mcp server.

## Postiz Social Media Tools

### __get_integrations_api_v1_postiz_integrations_get__

- __Purpose__: Get available Postiz social media integrations
- __Description__: Retrieve information about supported social media platforms and their integration status

### __schedule_post_api_v1_postiz_schedule_post__

- __Purpose__: Schedule a post to social media platforms
- __Description__: Schedule content to be posted to various social media platforms at a specified time

### __schedule_job_post_api_v1_postiz_schedule_job_post__

- __Purpose__: Schedule a post from a completed job result
- __Description__: Automatically schedule social media posts using content generated from completed jobs (videos, images, etc.)

### __schedule_post_now_api_v1_postiz_schedule_now_post__

- __Purpose__: Schedule a post to be published immediately
- __Description__: Post content to social media platforms right away without scheduling delay

### __create_draft_post_api_v1_postiz_create_draft_post__

- __Purpose__: Create a draft post
- __Description__: Create draft content for social media platforms that can be reviewed before publishing

These tools provide comprehensive social media management capabilities through Postiz integration, allowing you to schedule, draft, and immediately post content across multiple platforms.

### __Video Generation:__

- __create_video_generation_job_api_v1_videos_generations_post__ - Convert images to videos with Ken Burns effects, narration, and background music
- __generate_video_api_v1_videos_generate_post__ - Generate AI videos from text prompts using LTX-Video, WaveSpeed, or ComfyUI

## __Audio Creation Tools:__

- __create_speech_job_api_v1_audio_speech_post__ - Convert text to speech using Kokoro, Piper, or Edge TTS

### __Script Generation:__

- __generate_script_api_v1_ai_script_generate_post__ - Generate video scripts from topics using AI

__download_media_api_v1_media_download_post__ - Download media from URLs with intelligent format detection

source venv/bin/activate && python etugrand_agentos.py
