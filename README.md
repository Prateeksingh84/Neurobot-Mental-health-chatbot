# 🧠 NeuroBot – Mental Health Chatbot

## 📌 Overview
NeuroBot is a hybrid AI-powered mental health chatbot designed to offer real-time, context-aware, and empathetic emotional support. It combines a minimalistic Streamlit-based UI with LLaMA3 and a dynamic Gradio-based interface powered by Grok AI for advanced human-like interactions. NeuroBot aims to bridge the gap between technology and emotional well-being.

## 🧪 Abstract
NeuroBot addresses the growing global mental health crisis by providing a scalable, intelligent, and emotionally aware chatbot through hybrid AI systems. The chatbot delivers real-time cognitive behavioral responses, supports multimedia input using Base64 encoding, and ensures secure, private user interactions. It integrates the simplicity of Streamlit with the advanced capabilities of Gradio and Grok AI to simulate human-like therapeutic conversations.

## 🚀 Key Features
- Empathy-driven conversation using NLP and sentiment analysis.
- Hybrid architecture combining old (Streamlit + LLaMA3) and new (Gradio + Grok AI) systems.
- Real-time context memory and emotional feedback.
- Base64 encoding for secure multimedia handling.
- Anonymous usage, no user login required.
- Crisis detection with escalation prompts.

## 🏗️ Architecture

### Old Model
- **UI:** Streamlit  
- **Model:** LLaMA3 via Ollama  
- **Design:** Lightweight, minimalistic; ideal for offline or low-resource systems  

### New Model
- **UI:** Gradio  
- **Model:** Grok AI via Ollama  
- **Design:** Interactive, context-aware, supports multimedia input/output  

## 💡 Core Functionalities
- **Sentiment Analysis:** Understands emotional tone using NLP.
- **Conversational Memory:** Adapts responses based on previous dialogue.
- **Media Support:** Allows text, image, and voice input using Base64.
- **Model Switching:** Toggle between old and new models based on performance.
- **Security:** Anonymized sessions, optional logging, and data protection via Base64.

## 🛠️ Technologies Used
- Python 3.10+
- Streamlit & Gradio (UI)
- LLaMA3 & Grok AI (AI Models)
- Ollama (Model deployment)
- Base64 (Data encoding)
- Transformers, Requests, JSON

## 📦 Installation & Run

```bash
# For old model
streamlit run old_model.py

# For new model
python main.py
