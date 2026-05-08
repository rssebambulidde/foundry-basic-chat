# Azure AI Chat Applications

**SamaBrains Solution** | AI Engineering Project

Build simple conversational AI clients with Microsoft Foundry, Azure OpenAI,
the Responses API, streaming responses, and response ID based conversation
tracking.

## Project Overview

This repository contains two command-line chat implementations that demonstrate different Python concurrency patterns.

### `chat-app.py`: Synchronous Chat Application

- Uses a sequential request and response flow.
- Streams response text chunk by chunk.
- Tracks context with `previous_response_id`.
- Best for learning, demos, scripts, and simple chatbots.

### `chat-async.py`: Asynchronous Chat Application

- Uses `asyncio` and `AsyncOpenAI`.
- Streams response text with `async for`.
- Tracks context with `previous_response_id`.
- Best for web services, API servers, and high-concurrency applications.

## Quick Start

### 1. Set Up Python

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux, activate the environment with:

```bash
source venv/bin/activate
```

### 2. Configure Azure OpenAI

```bash
copy .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Edit `.env` and set:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/openai/v1
MODEL_DEPLOYMENT=gpt-4.1
```

### 3. Run a Chat App

```bash
# Synchronous version
python chat-app.py

# Asynchronous version
python chat-async.py
```

Type your prompts in the terminal. Type `quit` to exit.

## Key Features

- Responses API for simple model calls.
- Streaming output for responsive terminal chats.
- Conversation memory through response IDs.
- Token-based Azure authentication with `DefaultAzureCredential`.
- Basic configuration validation and graceful error output.

## Example Conversation

```text
Enter a prompt: Tell me about the ELIZA chatbot
Assistant: ELIZA is one of the earliest examples of natural language processing...

Enter a prompt: How does it compare to modern LLMs?
Assistant: Unlike ELIZA, modern LLMs like GPT-4 use deep learning...
```

The second prompt can refer to "it" because the app links turns with `previous_response_id`.

## Architecture

```text
User Input
    |
Responses API Request
    |
Azure OpenAI Model
    |
Streaming Response Events
    |
Display Text + Save Response ID
    |
Next Turn Uses previous_response_id
```

## Requirements

- Python 3.13 or later
- Azure subscription
- Azure OpenAI resource with a deployed model
- Microsoft Foundry or Azure OpenAI access
- Python packages from `requirements.txt`

## Repository Details

| Detail | Value |
| --- | --- |
| Repository | `rssebambulidde/foundry-basic-chat` |
| Remote URL | `https://github.com/rssebambulidde/foundry-basic-chat.git` |
| Current branch | `master` |
| Project type | Python command-line AI chat demo |
| Runtime | Python 3.13+ |
| Authentication | Azure Identity token authentication |
| Primary API | OpenAI Responses API through Azure OpenAI |
| License | MIT |
| CI workflow | GitHub Actions lint and formatting checks |

## Project Files

| File | Purpose |
| --- | --- |
| `chat-app.py` | Synchronous streaming chat client |
| `chat-async.py` | Asynchronous streaming chat client |
| `.env.example` | Environment variable template |
| `requirements.txt` | Runtime Python dependencies |
| `QUICKSTART.md` | Step-by-step setup guide |
| `ARCHITECTURE.md` | Design and flow details |
| `CONTRIBUTING.md` | Contribution guidelines |

## Comparison With Tools-Enhanced Chat

| Feature | This Project | Tools-Enhanced |
| --- | --- | --- |
| Chat functionality | Yes | Yes |
| Streaming | Yes | Yes |
| Conversation memory | Yes | Yes |
| Async implementation | Yes | No |
| File search | No | Yes |
| Web search | No | Yes |
| Primary use case | General Q&A | Knowledge-augmented AI |

## Troubleshooting

### Azure Credentials Not Found

Run:

```bash
az login
```

### Model Not Found

Check that `MODEL_DEPLOYMENT` in `.env` exactly matches your Azure OpenAI deployment name.

### Connection Timeout

- Verify that `AZURE_OPENAI_ENDPOINT` is correct.
- Check your internet connection.
- Confirm that your network allows access to the Azure OpenAI endpoint.

## Next Steps

- Try different system instructions in the scripts.
- Experiment with multi-turn conversations.
- Compare sync and async behavior.
- Use the async version as a starting point for a web API.

## Resources

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft Foundry](https://microsoft.com/foundry)
- [Async/Await in Python](https://docs.python.org/3/library/asyncio.html)
