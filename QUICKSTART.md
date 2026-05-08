
# Quick Start Guide

---

## 1. Prerequisites

```bash
# Check Python version (3.13+ required)
python --version

# Verify Git
git --version
```

---

## 2. Clone & Environment Setup

```bash
# Clone the repository
git clone <repository>
cd <project>

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 3. Configure Credentials

```bash
# Copy config template
copy .env.example .env
# or (on macOS/Linux)
cp .env.example .env

# Edit .env and add your Azure OpenAI credentials:
# AZURE_OPENAI_ENDPOINT=your_endpoint_url
# MODEL_DEPLOYMENT=gpt-4.1
```

---

## 4. Run Application

```bash
# Synchronous version (simpler)
python chat-app.py

# Asynchronous version (production)
python chat-async.py
```

---

## 5. Test It

```text
Enter a prompt: Tell me about ELIZA
Assistant: ELIZA is...

Enter a prompt: How does it compare to modern LLMs?
Assistant: Unlike ELIZA, modern LLMs...
(Note: AI remembered ELIZA!)

Enter a prompt: quit
```

---

## Azure Setup

### Login to Azure

```bash
az login
```

### Get Your Credentials

1. Go to [Azure Portal](https://portal.azure.com)
2. Search for "Azure OpenAI Service"
3. Find your service instance
4. Copy endpoint URL from "Keys and Endpoints"
5. Copy model deployment name

### Update .env

```env
AZURE_OPENAI_ENDPOINT=https://your-service.openai.azure.com/openai/v1
MODEL_DEPLOYMENT=gpt-4.1
```

---

## Architecture at a Glance

### Synchronous (`chat-app.py`)

- Sequential request/response
- Simple control flow
- Great for learning
- Not suitable for concurrent requests

### Asynchronous (`chat-async.py`)

- Non-blocking with async/await
- Handles 100s concurrent requests
- Production-ready
- More complex but efficient

---

## Key Features

- ✅ **Responses API** - Modern, simple API
- ✅ **Streaming** - Real-time token display
- ✅ **Context Memory** - Conversation tracking via response IDs
- ✅ **Token Auth** - Secure, no hardcoded keys
- ✅ **Error Handling** - Graceful failure modes

---

## Troubleshooting

### "Azure credentials not found"

```bash
az login
# Select your subscription when prompted
```

### "ModuleNotFoundError"

```bash
# Activate venv first
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### "Model not found"

```bash
# Check MODEL_DEPLOYMENT in .env
# Should exactly match your Azure deployment name
# Case-sensitive!
```

### "Connection timeout"

- Verify internet connection
- Check AZURE_OPENAI_ENDPOINT is correct
- Ensure not behind restrictive firewall

---

## Next Steps

1. **Explore the code** - Every line is commented
2. **Read ARCHITECTURE.md** - Deep dive into design
3. **Experiment** - Try different prompts
4. **Compare** - Run both sync and async versions
5. **Deploy** - See how async version scales

---

## File Structure

```text
.
├── chat-app.py              # Synchronous implementation
├── chat-async.py            # Asynchronous implementation
├── requirements.txt         # Python dependencies
├── .env.example            # Configuration template
├── .gitignore              # Git ignore rules
├── README.md               # Full documentation
├── ARCHITECTURE.md         # Design details
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # MIT License
└── .github/
    ├── workflows/
    │   └── lint.yml        # CI/CD pipeline
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Documentation

- **README.md** - Comprehensive guide
- **ARCHITECTURE.md** - Technical deep dive
- **Code comments** - Every function explained
- **In-code docstrings** - Function documentation

---

## Support

- 📧 **Contact:** [contact@samabrains.com](mailto:contact@samabrains.com)
- 🌐 **Website:** [samabrains.com](https://samabrains.com)
- 📚 **Docs:** See README.md and ARCHITECTURE.md

---

**Ready to build AI applications? Let's go!** 🚀
"