# Azure AI Chat Applications

**SamaBrains Solution** | AI Engineering Project  
*Building intelligent conversational AI with Microsoft Foundry and Azure OpenAI*

---

## 📋 Project Overview

Demonstration of modern AI chat architectures using **Responses API**, **streaming responses**, and **conversation tracking**. Two implementations showcase different concurrency patterns:

### **chat-app.py** - Synchronous Chat Application
- **Synchronous architecture** - Sequential request/response flow
- **Streaming responses** - Real-time token-by-token display
- **Conversation tracking** - Response IDs for context management
- **Use case:** Sequential chatbots, simple deployments, learning applications

### **chat-async.py** - Asynchronous Chat Application  
- **Asynchronous architecture** - Non-blocking async/await patterns
- **Concurrent handling** - Multiple conversations simultaneously
- **Same features** - Streaming, context tracking, response management
- **Use case:** Web services, API servers, production deployments, high-concurrency scenarios

## Quick Start

### 1. Setup
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure
```bash
# Copy the template
copy .env.example .env

# Edit .env and add your actual values:
# - AZURE_OPENAI_ENDPOINT: Your Azure OpenAI service endpoint
# - MODEL_DEPLOYMENT: Your model name (e.g., gpt-4.1)
```

### 3. Run

**Synchronous Version:**
```bash
python chat-app.py
```

**Asynchronous Version:**
```bash
python chat-async.py
```

Then type your prompts. Type `quit` to exit.

## Key Features

✅ **Responses API** - Modern, simple API (better than ChatCompletions)  
✅ **Streaming** - See responses appear in real-time  
✅ **Conversation Memory** - AI remembers previous exchanges  
✅ **Token-based Auth** - Secure (no hardcoded API keys)  
✅ **Error Handling** - Graceful error messages  

## Example Conversation

```
Enter a prompt: Tell me about the ELIZA chatbot
Assistant: ELIZA is one of the earliest examples of natural language processing...

Enter a prompt: How does it compare to modern LLMs?
Assistant: Unlike ELIZA, modern LLMs like GPT-4 use deep learning...
          (Note: AI remembered ELIZA from previous response!)
```

## Architecture

```
User Input
    ↓
Responses API Request
    ↓
Azure OpenAI Model (GPT-4.1)
    ↓
Streaming Response (chunks arrive)
    ↓
Display to User + Save Response ID
    ↓
Next turn links via previous_response_id
```

## Requirements

- Python 3.13+
- Azure Subscription
- Azure OpenAI Service with deployed model
- microsoft-foundry access
- Packages: openai, azure-identity, python-dotenv, aiohttp

## For Learning

**New to AI/Coding?** Check the comments in the code - every line is explained!

**Want to understand?**
- `chat-app.py` - Simpler, synchronous flow (easier to follow)
- `chat-async.py` - More advanced, async patterns (requires async knowledge)

## Comparison with Tools-Enhanced Version

| Feature | This Project | Tools-Enhanced |
|---------|------------|-----------------|
| Chat Functionality | ✅ | ✅ |
| Streaming | ✅ | ✅ |
| Conversation Memory | ✅ | ✅ |
| Non-blocking (async) | Only in chat-async.py | Not available |
| File Search (PDFs) | ❌ | ✅ |
| Web Search | ❌ | ✅ |
| Use Case | General Q&A | Knowledge-augmented AI |

## Troubleshooting

**"Azure credentials not found"**
- Run `az login` to authenticate with Azure

**"Model not found"**
- Check MODEL_DEPLOYMENT in .env matches your actual deployment

**"Connection timeout"**
- Verify AZURE_OPENAI_ENDPOINT is correct
- Check internet connection

## Next Steps

- Try different system prompts to customize the AI's personality
- Experiment with multi-turn conversations
- Compare sync vs async performance
- Explore the tools-enhanced version for advanced capabilities

## Resources

- [OpenAI Python SDK Docs](https://github.com/openai/openai-python)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft Foundry Docs](https://microsoft.com/foundry)
- [Async/Await in Python](https://docs.python.org/3/library/asyncio.html)
