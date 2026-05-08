# Quick Start Guide

## 1. Prerequisites

```bash
# Check Python version
python --version

# Verify Git
git --version
```

This project is designed for Python 3.13 or later.

## 2. Clone and Set Up the Environment

```bash
# Clone the repository
git clone <repository>
cd <project>

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## 3. Configure Credentials

```bash
# Copy the config template
copy .env.example .env

# macOS/Linux alternative
cp .env.example .env
```

Update `.env` with your Azure OpenAI values:

```env
AZURE_OPENAI_ENDPOINT=https://your-service.openai.azure.com/openai/v1
MODEL_DEPLOYMENT=gpt-4.1
```

## 4. Sign In to Azure

```bash
az login
```

Select the subscription that contains your Azure OpenAI resource.

## 5. Run the Application

```bash
# Synchronous version
python chat-app.py

# Asynchronous version
python chat-async.py
```

Type your prompts at the terminal. Type `quit` to exit.

## 6. Try a Multi-Turn Conversation

```text
Enter a prompt: Tell me about ELIZA
Assistant: ELIZA is...

Enter a prompt: How does it compare to modern LLMs?
Assistant: Unlike ELIZA, modern LLMs...

Enter a prompt: quit
```

The second response can use context from the first exchange because the app passes `previous_response_id` between turns.

## Azure Setup

To find your Azure OpenAI values:

1. Open the [Azure Portal](https://portal.azure.com).
2. Search for your Azure OpenAI resource.
3. Open the resource's keys and endpoint page.
4. Copy the endpoint URL.
5. Copy the model deployment name from Azure AI Foundry or Azure OpenAI Studio.

## Architecture at a Glance

### Synchronous App (`chat-app.py`)

- Uses a sequential request and response flow.
- Streams response chunks as they arrive.
- Is easiest to follow while learning.

### Asynchronous App (`chat-async.py`)

- Uses `asyncio` and `AsyncOpenAI`.
- Streams response chunks with `async for`.
- Fits better into web services or other async Python applications.

## Key Features

- Responses API
- Streaming token output
- Conversation context through response IDs
- Token-based Azure authentication
- Basic environment validation and error handling

## Troubleshooting

### Azure Credentials Not Found

```bash
az login
```

Make sure the selected subscription has access to the Azure OpenAI resource.

### Missing Python Package

```bash
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Model Not Found

Check that `MODEL_DEPLOYMENT` in `.env` exactly matches your deployed model name. Deployment names are case-sensitive.

### Connection Timeout

- Verify your internet connection.
- Check that `AZURE_OPENAI_ENDPOINT` is correct.
- Confirm that your network or firewall allows access to the endpoint.

## File Structure

```text
.
├── chat-app.py              # Synchronous implementation
├── chat-async.py            # Asynchronous implementation
├── requirements.txt         # Python dependencies
├── .env.example             # Configuration template
├── .gitignore               # Git ignore rules
├── README.md                # Full documentation
├── ARCHITECTURE.md          # Design details
├── CONTRIBUTING.md          # Contribution guidelines
├── LICENSE                  # MIT License
└── .github/
    ├── workflows/
    │   └── lint.yml         # CI workflow
    └── PULL_REQUEST_TEMPLATE.md
```

## Next Steps

1. Explore the code.
2. Read `ARCHITECTURE.md`.
3. Try different prompts.
4. Compare the sync and async implementations.
5. Adapt the async version for a web API or service.

## Support

- Contact: [info@samabrains.com](mailto:contact@samabrains.com)
- Website: [samabrains.com](https://samabrains.com)
- Docs: See `README.md` and `ARCHITECTURE.md`
