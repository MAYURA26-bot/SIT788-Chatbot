# Multimodal Vehicle Recommendation Assistant

This project is a smart, multimodal AI assistant designed to recommend vehicles based on user preferences. The assistant supports both **text** and **voice input**, processes natural language queries using **Azure OpenAI (GPT)**, and responds in both **text and synthesized audio** formats using **Azure Text-to-Speech**.



## Features

-  Voice input support (speech-to-text via Azure)
-  Natural language understanding (Azure OpenAI Chat Completion)
-  Voice responses (text-to-speech output)
-  Tailored vehicle suggestions based on a rich dataset
-  User-friendly Bootstrap chat interface
-  Django-based backend with clear modular structure


##  How It Works

### 1. Text Mode:
- User types a vehicle-related query.
- Backend sends both query and dataset to Azure OpenAI GPT.
- GPT filters and returns the best match.
- The response is converted to audio (Text-to-Speech).
- User receives the original query, GPT response, and audio.

### 2. Voice Mode:
- User presses and holds the microphone button to record.
- Audio is sent to Azure Speech-to-Text for transcription.
- Transcribed text is sent to GPT for response.
- GPT output is converted to audio.
- User receives transcribed input, GPT response, and voice reply.




