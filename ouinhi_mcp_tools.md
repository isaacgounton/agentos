# Ouinhi MCP Tools

This document provides a comprehensive overview of all available tools in the Ouinhi MCP server, with detailed descriptions of their capabilities and use cases for agents. Each tool is designed to enable powerful multimedia processing, AI content generation, and social media automation workflows.

## check_job_status

**Description:** Check the status of an asynchronous job by its ID. This tool is essential for monitoring async operations like video generation, image processing, audio conversion, etc. Most API operations return a job ID immediately, and you must use this tool to check when the job is complete and get the final result. For agents, this is crucial for managing long-running tasks, tracking progress, and retrieving results once processing is finished. It allows agents to poll job status periodically until completion, enabling efficient workflow management in automated content creation pipelines.

## async_workflow_guide

**Description:** Get guidance on how to use asynchronous operations in this API. This API uses async processing for most operations (video generation, image processing, etc.). Understanding the workflow is crucial for successful usage. For agents, this tool provides essential knowledge about handling async jobs, including how to initiate operations, monitor progress, and handle completion callbacks. It's particularly useful for agents building automated workflows that need to coordinate multiple async tasks.

## list_tools

**Description:** List all available tools in this MCP server. This tool provides a comprehensive overview of all registered tools, including dynamically registered OpenAPI tools (filtered for usefulness) and manual tools (check_job_status, async_workflow_guide, list_tools). For agents, this is invaluable for discovering available functionality, understanding tool capabilities, and planning workflows with available tools. Agents can use this to dynamically adapt their behavior based on available tools and build flexible automation systems.

## create_video_generation_job_api_v1_videos_generations_post

**Description:** Create an optimized job to convert an image to a video with optional audio and captions. Supports both synchronous and asynchronous generation modes. This tool enables agents to create engaging video content from static images, adding dynamic effects like Ken Burns zoom, narration, background music, and captions. Perfect for agents automating social media content creation, educational videos, or marketing materials. The async mode allows agents to handle large-scale video production without blocking other operations.

## edit_image_api_v1_images_edit_post

**Description:** Edit an image using AI models (currently supports Flux only). Creates an asynchronous job that edits an uploaded image using Flux Kontext Dev model. For agents, this enables sophisticated image manipulation capabilities, including photo editing, style transfer, object addition/removal, and creative transformations. Ideal for agents working on content creation, design automation, or visual content enhancement workflows.

## create_video_edit_job_api_v1_videos_edit_post

**Description:** Create a job to overlay videos on top of a base image. This endpoint processes a request to overlay one or more videos onto a base image, creating dynamic video compositions with precise control over positioning, timing, size, and audio mixing. For agents, this tool enables complex video compositing operations, perfect for creating layered content, advertisements, or interactive media. The precise control over positioning and timing makes it ideal for automated video production pipelines.

## generate_image_api_v1_images_generate_post

**Description:** Generate high-quality AI images from text prompts. This endpoint creates stunning images using state-of-the-art AI models with support for both synchronous and asynchronous processing modes. For agents, this provides powerful image generation capabilities for content creation, marketing materials, social media graphics, and automated design workflows. The multiple model support and customizable parameters allow agents to generate images tailored to specific needs and quality requirements.

## simple_edit_image_api_v1_images_edit_image_post

**Description:** Simple image editing endpoint for external compatibility. This endpoint provides a straightforward interface for image editing with API key authentication, making it compatible with external services like n8n and other automation tools. For agents, this offers a simplified interface for image editing operations, ideal for integration with broader automation platforms and workflows that require straightforward image manipulation without complex parameters.

## create_image_enhancement_job_api_v1_images_enhance_post

**Description:** Create a job to enhance an image by removing AI artifacts and adding natural imperfections. This endpoint processes a request to enhance images by removing AI-generated artifacts and adjusting color saturation and contrast for more authentic look. For agents, this tool is essential for post-processing AI-generated images, making them appear more natural and professional. Perfect for agents creating realistic content or preparing images for professional use.

## create_speech_job_api_v1_audio_speech_post

**Description:** Create a job to convert text to speech using the specified TTS provider with advanced features. This endpoint supports multiple TTS providers: Kokoro TTS, Piper TTS, and Edge TTS. For agents, this enables high-quality voice synthesis for narration, audiobooks, voiceovers, and accessibility features. The multiple provider support allows agents to choose voices based on quality, speed, and language requirements for diverse content creation needs.

## list_audio_voices_api_v1_audio_voices_get

**Description:** List available voices for audio generation (OpenAI-compatible format). Returns a dictionary with voices list. For agents, this tool helps discover available voice options for TTS operations, enabling dynamic voice selection based on content type, target audience, or stylistic requirements. Essential for agents building voice-enabled applications or automated audio content creation.

## list_audio_voices_api_v1_audio_voices_post

**Description:** List available voices for audio generation (OpenAI-compatible format). Returns a dictionary with voices list. Similar to the GET version, this provides agents with programmatic access to voice inventories for automated voice selection and content planning.

## get_voices_formatted_api_v1_audio_voices_formatted_get

**Description:** Get formatted list of voices by provider (OpenAI-compatible format). For agents, this organizes voice options by provider, making it easier to select appropriate voices for specific use cases and maintain consistency across different TTS operations.

## get_all_voices_api_v1_audio_voices_all_get

**Description:** Get all available voices from all providers. For agents, this provides a comprehensive view of all available voices across providers, enabling sophisticated voice selection algorithms and fallback mechanisms for robust audio generation workflows.

## list_audio_models_api_v1_audio_models_get

**Description:** List available audio/TTS models (OpenAI-compatible format). Returns a dictionary with models list. For agents, this helps identify available TTS models and their capabilities, allowing for model selection based on quality, speed, and feature requirements.

## list_audio_models_api_v1_audio_models_post

**Description:** List available audio/TTS models (OpenAI-compatible format). Returns a dictionary with models list. Provides programmatic access to model information for automated model selection in agent workflows.

## get_models_formatted_api_v1_audio_models_formatted_get

**Description:** Get formatted list of TTS models (OpenAI-compatible format). For agents, this organizes model information in a structured format, facilitating automated decision-making for TTS model selection based on specific requirements.

## get_supported_providers_api_v1_audio_providers_get

**Description:** Get list of supported TTS providers and their capabilities. For agents, this provides detailed information about available providers, their features, and supported formats, enabling intelligent provider selection for different use cases.

## get_tts_providers_api_v1_audio_tts_providers_get

**Description:** Get TTS providers for frontend compatibility. For agents, this offers provider information formatted for easy integration with user interfaces or other systems requiring TTS provider details.

## get_voices_for_provider_api_v1_audio_tts__provider__voices_get

**Description:** Get voices for a specific provider for frontend compatibility. For agents, this allows targeted voice discovery for specific providers, useful for building provider-specific voice selection interfaces or workflows.

## create_transcriptions_job_api_v1_audio_transcriptions_post

**Description:** Create a job to transcribe media using Whisper. This endpoint accepts a media URL and transcribes it using Whisper. For agents, this enables automatic speech-to-text conversion for audio/video content, perfect for content analysis, accessibility features, search indexing, and automated caption generation.

## download_media_api_v1_media_download_post

**Description:** Download any file from a URL with intelligent format detection. This endpoint supports media platforms (YouTube, Vimeo, Twitter, etc.) using yt-dlp, and direct file downloads. For agents, this provides robust media acquisition capabilities, enabling automated content gathering from various online sources for processing and analysis.

## extract_metadata_api_v1_media_metadata_post

**Description:** Extract metadata from a media file including video/audio properties. This endpoint analyzes a media file and returns comprehensive metadata. For agents, this is crucial for content analysis, quality assessment, format detection, and automated media processing workflows.

## create_concatenate_job_api_v1_videos_concatenate_post

**Description:** Create a job to concatenate multiple videos into a single video with transition effects. This endpoint supports professional transition effects between video segments. For agents, this enables automated video editing workflows, creating seamless compilations, tutorials, or promotional content with professional transitions.

## create_add_audio_job_api_v1_videos_add_audio_post

**Description:** Create a job to add audio to a video with advanced sync modes and fade effects. This endpoint supports multiple audio synchronization modes: replace, mix, overlay. For agents, this provides sophisticated audio-video synchronization capabilities for creating professional video content with precise audio control.

## create_merge_job_api_v1_videos_merge_post

**Description:** Create a job to merge multiple videos with optional background audio. This endpoint combines video concatenation with audio overlay functionality. For agents, this enables complex video production workflows, perfect for creating comprehensive content packages with synchronized audio and video elements.

## create_add_captions_job_api_v1_videos_add_captions_post

**Description:** Create a job to add captions to a video. Supports both synchronous and asynchronous caption addition modes. For agents, this automates accessibility features and content enhancement, making videos more inclusive and searchable through automatic caption generation.

## create_text_overlay_job_api_v1_videos_text_overlay_post

**Description:** Create a job to add text overlay to a video. This endpoint adds customizable text overlays with extensive styling options. For agents, this enables dynamic text addition to videos for branding, information display, or interactive content creation.

## get_text_overlay_presets_api_v1_videos_text_overlay_presets_get

**Description:** Get available text overlay presets. Returns a comprehensive list of predefined text overlay styles optimized for different use cases. For agents, this provides quick access to professional styling options for consistent text overlay application across content.

## create_text_overlay_with_preset_api_v1_videos_text_overlay_preset__preset_name__post

**Description:** Add text overlay using predefined preset. Apply professional text overlays using optimized presets for common use cases. For agents, this enables rapid application of professional text styling without manual configuration.

## create_modern_text_overlay_job_api_v1_videos_modern_text_overlay_post

**Description:** Create modern text overlay with advanced features including animations, effects, and smart positioning. For agents, this provides cutting-edge text overlay capabilities with animations and effects for engaging, modern video content.

## get_modern_text_overlay_presets_api_v1_videos_modern_presets_get

**Description:** Get modern text overlay presets with advanced styling options. Returns comprehensive modern presets designed for social media, video platforms, and creative applications. For agents, this offers access to trendy, platform-optimized text styling for maximum engagement.

## create_modern_preset_overlay_api_v1_videos_modern_preset__preset_name__post

**Description:** Create text overlay using modern preset with optional customization. For agents, this enables quick application of modern text styles with customization options for brand consistency and creative expression.

## generate_text_overlay_preview_api_v1_videos_preview_post

**Description:** Generate a fast preview of text overlay for real-time feedback. For agents, this allows quick preview generation for testing text overlay configurations before full processing, improving workflow efficiency.

## get_all_text_overlay_presets_api_v1_videos_all_presets_get

**Description:** Get both legacy and modern text overlay presets combined. For agents, this provides a unified view of all available text styling options for comprehensive content creation capabilities.

## create_thumbnails_job_api_v1_videos_thumbnails_post

**Description:** Create a job to generate thumbnails from a video. For agents, this automates thumbnail creation for video content, essential for social media optimization and content discoverability.

## generate_video_api_v1_videos_generate_post

**Description:** Generate an AI video from a text prompt using your choice of AI video provider. Supports multiple providers like LTX Video, WaveSpeed, and ComfyUI. For agents, this enables AI-powered video creation from text descriptions, perfect for automated content generation and creative workflows.

## generate_video_from_image_api_v1_videos_from_image_post

**Description:** Generate a video from an image using LTX-Video. Creates an asynchronous job that animates an uploaded image using the LTX-Video model. For agents, this brings static images to life, creating dynamic content from existing visual assets.

## convert_media_api_v1_conversions__post

**Description:** Convert media files between formats using FFmpeg with comprehensive format support. For agents, this provides universal media conversion capabilities, enabling format standardization and compatibility across different platforms and devices.

## generate_script_api_v1_ai_script_generate_post

**Description:** Generate a video script from a topic using AI. Supports multiple script types: facts, story, educational. For agents, this automates script writing for video content, enabling rapid content ideation and production planning.

## generate_script_api_v1_ai_script_generation_post

**Description:** Generate a video script from a topic using AI. Similar to the above, with support for auto-topic discovery. For agents, this provides intelligent content generation with trending topic integration.

## research_topic_api_v1_ai_news_research_post

**Description:** Research a topic using news APIs to gather recent information. Creates an asynchronous job to research topics using Google Search and Perplexity APIs. For agents, this enables automated research and content gathering for timely, relevant content creation.

## research_topic_frontend_api_v1_ai_research_topic_post

**Description:** Research a topic for frontend compatibility. For agents, this provides research capabilities optimized for user-facing applications and interfaces.

## generate_video_search_queries_api_v1_ai_video_search_queries_post

**Description:** Generate video search queries from script content using AI. For agents, this automates the process of finding relevant background videos for scripted content, streamlining video production workflows.

## search_stock_videos_api_v1_ai_video_search_stock_videos_post

**Description:** Search for stock videos using the Pexels API. For agents, this provides access to high-quality stock footage for content creation, enabling automated video sourcing and production.

## browse_stock_videos_api_v1_ai_video_browse_post

**Description:** Browse stock videos with simple search interface. For agents, this offers a straightforward interface for video asset discovery and selection.

## search_stock_images_api_v1_ai_image_search_stock_images_post

**Description:** Search for stock images using Pexels or Pixabay APIs. For agents, this enables automated image sourcing for content creation, marketing materials, and visual content workflows.

## generate_video_from_script_with_ai_images_api_v1_ai_aiimage_to_video_post

**Description:** Generate a complete video from a script using AI-generated images. This comprehensive tool handles the entire pipeline from script to final video. For agents, this represents a complete automated content creation solution, from ideation to finished product.

## generate_ai_content_api_v1_ai_generate_post

**Description:** Generate AI content from a text prompt using OpenAI or Groq. For agents, this provides flexible AI content generation capabilities with provider selection for different quality and speed requirements.

## get_supported_formats_api_v1_documents_formats_get

**Description:** Get list of supported input/output formats and features. For agents, this helps understand document processing capabilities for planning conversion and analysis workflows.

## convert_document_to_markdown_api_v1_documents_to_markdown_post

**Description:** Convert documents to Markdown format using Microsoft MarkItDown. Supports various document formats including PDF, Word, Excel, etc. For agents, this enables document processing and content extraction for analysis and repurposing.

## convert_document_to_markdown_simple_api_v1_documents_to_markdown_simple_post

**Description:** Convert documents to Markdown format (synchronous version). For agents, this provides fast document conversion for smaller files in synchronous workflows.

## extract_structured_data_api_v1_documents_langextract_post

**Description:** Extract structured data from text using AI-powered analysis. Uses Google Langextract for entity extraction and relationship analysis. For agents, this enables intelligent data extraction from unstructured documents for automated processing and analysis.

## extract_structured_data_json_api_v1_documents_langextract_json_post

**Description:** Extract structured data from text using JSON request format. For agents, this provides programmatic access to structured data extraction with flexible input options.

## list_models_api_v1_models_get

**Description:** List available TTS models (OpenAI-compatible format). For agents, this provides model discovery for TTS operations with OpenAI-compatible interfaces.

## list_models_api_v1_models_post

**Description:** List available TTS models (OpenAI-compatible format). Provides programmatic access to model listings for automated workflows.

## list_voices_api_v1_voices_get

**Description:** List Edge TTS voices with optional language filtering. For agents, this enables voice discovery and selection for TTS applications.

## list_voices_api_v1_voices_post

**Description:** List Edge TTS voices with optional language filtering. Provides programmatic voice listing capabilities.

## list_all_voices_api_v1_voices_all_get

**Description:** List all available Edge TTS voices. For agents, this offers comprehensive voice inventories for advanced TTS applications.

## list_all_voices_api_v1_voices_all_post

**Description:** List all available Edge TTS voices. Provides complete voice access for agent workflows.

## elevenlabs_text_to_speech_api_v1_elevenlabs_text_to_speech__voice_id__post

**Description:** ElevenLabs-compatible text-to-speech endpoint. For agents, this enables integration with ElevenLabs TTS services for high-quality voice synthesis.

## azure_cognitive_services_tts_api_v1_azure_cognitiveservices_v1_post

**Description:** Azure Cognitive Services-compatible text-to-speech endpoint. For agents, this provides access to Azure's enterprise-grade TTS capabilities.

## get_job_status_api_jobs__job_id__status_get

**Description:** Get the status and result of a specific job. For agents, this is essential for monitoring async operations and retrieving completed results.

## check_api_keys_api_diagnostics_api_keys_get

**Description:** Check which API keys are configured. For agents, this enables diagnostic capabilities to ensure service availability and troubleshoot configuration issues.

## check_service_health_api_diagnostics_service_health_get

**Description:** Check the health of all AI services. For agents, this provides system health monitoring for reliable operation and issue detection.

## get_integrations_api_v1_postiz_integrations_get

**Description:** Get available Postiz social media integrations. For agents, this enables discovery of available social media platforms for automated posting and scheduling.

## schedule_post_api_v1_postiz_schedule_post

**Description:** Schedule a post to social media platforms. For agents, this automates social media content scheduling and publishing workflows.

## schedule_job_post_api_v1_postiz_schedule_job_post

**Description:** Schedule a post from a completed job result. For agents, this enables automated publishing of generated content to social media platforms.

## schedule_post_now_api_v1_postiz_schedule_now_post

**Description:** Schedule a post to be published immediately. For agents, this provides instant publishing capabilities for time-sensitive content.

## create_draft_post_api_v1_postiz_create_draft_post

**Description:** Create a draft post. For agents, this enables draft creation for review and approval workflows before publishing.

## list_videos_api_v1_videos__get

**Description:** Get list of videos with filtering and pagination. For agents, this provides video library management and search capabilities.

## get_video_api_v1_videos__video_id__get

**Description:** Get detailed video information by ID. For agents, this enables detailed video metadata retrieval for content analysis and management.

## update_video_api_v1_videos__video_id__put

**Description:** Update video metadata. For agents, this allows programmatic video metadata management and organization.

## delete_video_api_v1_videos__video_id__delete

**Description:** Soft delete a video. For agents, this provides content lifecycle management capabilities.

## download_video_api_v1_videos__video_id__download_get

**Description:** Get download URL for video or related files. For agents, this enables automated content distribution and access.

## get_video_stats_api_v1_videos_stats_overview_get

**Description:** Get video statistics overview. For agents, this provides analytics and performance insights for content optimization.

## get_caption_style_presets_api_v1_videos_caption_styles_presets_get

**Description:** Get all available caption style presets with their default values. For agents, this offers access to professional caption styling for consistent video production.

## get_caption_style_preset_details_api_v1_videos_caption_styles_presets__style_name__get

**Description:** Get detailed preset configuration for a specific caption style. For agents, this enables detailed preset inspection for customization.

## apply_caption_style_preset_endpoint_api_v1_videos_caption_styles_apply_preset_post

**Description:** Apply a caption style preset to current parameters, preserving user overrides. For agents, this streamlines caption styling with intelligent preset application.

## get_style_recommendations_endpoint_api_v1_videos_caption_styles_recommendations_get

**Description:** Get caption style recommendations for specific content types. For agents, this provides intelligent styling recommendations based on content type.

## get_caption_best_practices_endpoint_api_v1_videos_caption_styles_best_practices_get

**Description:** Get caption best practices and guidelines. For agents, this offers expert guidance for optimal caption implementation.

## get_library_content_api_v1_library_content_get

**Description:** Retrieve organized content from the persistent media library. For agents, this provides comprehensive content management and access capabilities.

## get_content_item_api_v1_library_content__media_id__get

**Description:** Get a specific content item by media ID. For agents, this enables targeted content retrieval for specific workflows.

## delete_content_item_api_v1_library_content__media_id__delete

**Description:** Soft delete a content item (marks as deleted, doesn't remove from S3). For agents, this provides content lifecycle management.

## scan_s3_for_content_api_v1_library_scan_s3_post

**Description:** Scan S3 bucket for content that might not be in the database. For agents, this enables content discovery and synchronization.

## schedule_content_item_api_v1_library_content__media_id__schedule_post

**Description:** Schedule a library content item to social media via Postiz. For agents, this automates content publishing from the library.

## generate_image_api_pollinations_image_generate_post

**Description:** Generate an image using Pollinations.AI. For agents, this provides additional image generation capabilities with Pollinations.AI integration.

## analyze_image_vision_api_pollinations_vision_analyze_post

**Description:** Analyze an image using Pollinations Vision API. For agents, this enables AI-powered image analysis and understanding.

## analyze_uploaded_image_api_pollinations_vision_analyze_upload_post

**Description:** Analyze an uploaded image using Pollinations Vision API. For agents, this provides image analysis for uploaded content.

## list_image_models_api_pollinations_models_image_get

**Description:** List available Pollinations image generation models. For agents, this helps discover available image generation models.

## list_text_models_api_pollinations_models_text_get

**Description:** List available Pollinations text/vision models and voices. For agents, this provides model discovery for text and vision tasks.

## generate_text_api_pollinations_text_generate_post

**Description:** Generate text using Pollinations.AI Text API. For agents, this offers additional text generation capabilities.

## create_chat_completion_api_pollinations_chat_completions_post

**Description:** Create a chat completion using Pollinations.AI Chat API. For agents, this enables advanced conversational AI interactions.

## text_to_speech_api_pollinations_audio_tts_post

**Description:** Generate speech audio from text using Pollinations.AI TTS. For agents, this provides additional TTS capabilities.

## transcribe_audio_api_pollinations_audio_transcribe_post

**Description:** Transcribe audio file using Pollinations.AI STT. For agents, this enables speech-to-text conversion with Pollinations.AI.

## list_available_voices_api_pollinations_voices_get

**Description:** List available TTS voices for Pollinations audio generation. For agents, this helps discover available voices for TTS.

## login_auth_login_post

**Description:** Authenticate with username and password and return API key. For agents, this enables programmatic authentication for API access.

## health_check_health_get

**Description:** Simple health check endpoint for container health monitoring. For agents, this provides system health verification capabilities.
