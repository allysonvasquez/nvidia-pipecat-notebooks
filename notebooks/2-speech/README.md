# Module 2: Speech – Digital Human Teaching Kit

Welcome to the Speech module of the Digital Human Teaching Kit. This module provides a hands-on, application-oriented exploration of real-time speech pipelines for digital humans, leveraging NVIDIA Pipecat and ACE Controller. It is designed for a master's level audience seeking both practical skills and a deep conceptual understanding of speech-driven AI agents.

## Module Purpose and Context

Module 2 focuses on the technical and architectural foundations of speech-to-speech (S2S) pipelines, which are central to interactive digital human systems. Here, you will build, analyze, and extend pipelines that convert live audio into text, generate intelligent responses, and synthesize natural-sounding speech—all in real time. The module bridges core speech technologies (ASR, TTS), large language models (LLMs), and the modular, low-latency design patterns required for believable digital humans.

### Learning Objectives
- Articulate the role of speech pipelines in digital human applications.
- Implement and experiment with modular ASR, TTS, and LLM components using NVIDIA Pipecat.
- Analyze real-time constraints, streaming data flows, and latency in conversational AI.
- Critically evaluate and extend speech pipelines for research or production use.

## Pedagogical Flow & Recommended Order
1. **0-Primer-NVIDIA-Pipecat.ipynb**: Provides a conceptual and practical introduction to the Pipecat framework and its modular pipeline architecture. Essential for understanding how ASR, TTS, and LLM processors are composed and orchestrated.
2. **1-ASR-basics.ipynb**: Deep dive into Automatic Speech Recognition (ASR) using NVIDIA Riva. Learn to transcribe audio streams and experiment with streaming vs. batch modes, interim results, and language support.
3. **2-TTS-basics.ipynb**: Practical exploration of Text-to-Speech (TTS) synthesis. Covers Riva TTS configuration, voice selection, and integration into the pipeline. Encourages experimentation with different voices and languages.
4. **3-Voice-Agent.ipynb**: Capstone notebook for Module 2. Guides you through building a real-time, voice-enabled conversational agent. Integrates ASR, LLM, and TTS with context aggregation and WebSocket transport. Includes a sample system prompt for a museum guide agent.

## Notebook Summaries

- **0-Primer-NVIDIA-Pipecat.ipynb**: Introduces the Pipecat and ACE Controller frameworks, explaining the concepts of frames, processors, and pipelines. Discusses how modularity and streaming enable low-latency, real-time digital human behaviors, and provides the foundational mental model for the rest of the module.

- **1-ASR-basics.ipynb**: Hands-on with Automatic Speech Recognition. Demonstrates setup, streaming transcription, and the use of NVIDIA Riva ASR within Pipecat. Discusses interim results, interruption handling, and language support.

- **2-TTS-basics.ipynb**: Practical exploration of Text-to-Speech synthesis. Covers Riva TTS configuration, voice selection, and integration into the pipeline. Encourages experimentation with different voices and languages.

- **3-Voice-Agent.ipynb**: Capstone notebook for Module 2. Guides you through building a real-time, voice-enabled conversational agent. Integrates ASR, LLM, and TTS with context aggregation and WebSocket transport. Demonstrates end-to-end pipeline assembly and deployment via ACE Controller.

## Speech Pipeline Architecture: ASR, LLM, TTS, and Modularity

The digital human speech pipeline is architected for modularity, real-time streaming, and low latency. Each component fulfills a distinct role:

- **ASR (Automatic Speech Recognition)**: Captures and transcribes user speech to text, often with Voice Activity Detection (VAD) for responsiveness.
- **LLM (Large Language Model)**: Generates contextually appropriate, intelligent responses based on the transcribed input and conversation history.
- **TTS (Text-to-Speech)**: Synthesizes natural-sounding audio from the LLM's text output, enabling expressive, real-time voice responses.

These components are orchestrated in a Pipecat pipeline, where each processor transforms data frames and passes them downstream. The modular design allows for easy swapping of models, adaptation to new modalities (e.g., vision), and deployment across diverse environments (local, cloud, containerized, or ACE Controller microservices).

## Further Exploration

For advanced students and researchers, consider the following directions:
- **Model Swapping**: Replace Riva ASR/TTS with alternative models (open-source, multilingual, or domain-specific).
- **Latency Measurement**: Instrument the pipeline to measure and analyze end-to-end and component-wise latency. Investigate trade-offs between streaming and batch processing.
- **Proactivity and Tool Use**: Experiment with agent proactivity (interruptions, reminders) and tool-calling (API/database access) via LLM extensions.
- **Deployment Scenarios**: Explore deployment on edge devices, in containers, or as scalable microservices using ACE Controller.
- **Human Factors**: Study the impact of voice quality, latency, and conversational flow on user experience and believability.

---

This module is intended as both a practical lab and a foundation for research in digital human speech systems. For questions, contributions, or deeper technical references, consult the main repository README and the official Pipecat and ACE Controller documentation. 