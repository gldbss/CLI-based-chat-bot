# OpenRouter CLI AI Chatbot

A simple AI-powered CLI chatbot built with Python using the OpenRouter API.

This chatbot can run directly from:

- Windows CMD / PowerShell
- Linux Terminal
- macOS Terminal

It supports:
- Multiple AI models
- Persistent chat history
- Text-to-speech responses
- Loading previous conversations
- OpenRouter API integration

---

# Features

- Interactive terminal chatbot
- OpenRouter API support
- Select between multiple models
- Save and load chat history
- Speech output using `pyttsx3`
- Works cross-platform
- JSON-based conversation storage

---

# Supported Models

Currently includes support for:

- `openrouter/owl-alpha`
- `inclusionai/ring-2.6-1t:free`
- `baidu/cobuddy:free`
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- `poolside/laguna-xs.2:free`
- `poolside/laguna-m.1:free`
- `google/gemma-4-26b-a4b-it:free`
- `google/gemma-4-31b-it:free`

You can easily add more models inside `main.py`.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

---

## 2. Install Requirements

```bash
pip install requests python-dotenv pyttsx3
```

---

# OpenRouter API Key Setup

Create an API key from:

https://openrouter.ai/

Run the program once:

```bash
python setup.py
```

If `.env` does not exist, the program will automatically ask for your API key and create the file.

Generated `.env`:

```env
API_KEY=your_api_key_here
```

---

# Running the Chatbot

```bash
python setup.py
```

---

# Usage

On startup:

```text
1> pre set
2> select optimum
```

## Option 1
Uses a predefined model.

## Option 2
Lets you select a model manually.

---

# Chat History

Chat histories are automatically saved as JSON files inside:

```text
files.fxg/
```

You can reopen previous chats by entering the chat ID during startup.

---

# Text To Speech

After every response:

```text
speak up?:
```

Type:

```text
Y
```

to hear the AI response spoken aloud.

---

# Project Structure

```text
.
├── main.py
├── setup.py
├── comm_ai_mod.py
├── hist_chat_name_builder.py
├── speak.py
├── files.fxg/
└── .env
```

---

# Example

```text
User:
Hello

Model:
Hi! How can I help you today?
```

---

# Requirements

- Python 3.10+
- Internet connection
- OpenRouter API key

---

# Notes

- Some free OpenRouter models may occasionally become rate limited.
- Chat histories are stored locally.
- Works best in modern terminals.

---

# Future Improvements

- Streaming responses
- Better error handling
- Conversation search
- GUI version
- Voice input
- Markdown rendering in terminal

---

# License

This project currently has no public license.

---

# Author

Built using Python + OpenRouter API.
