# Architecture Overview

This project demonstrates two small Azure OpenAI chat clients that share the
same behavior but use different execution models.

## Synchronous Chat Application (`chat-app.py`)

```text
User Input
    |
OpenAI Client
    |
Responses API Request
    |
Azure OpenAI Model
    |
Streaming Response Events
    |-- response.output_text.delta -> Display text chunk
    `-- response.completed -> Save response ID
    |
Next Turn Uses previous_response_id
```

### Flow

1. The user enters a prompt.
2. The client sends a synchronous Responses API request.
3. The model streams text events back to the terminal.
4. The app prints each text delta immediately.
5. The app stores the completed response ID for the next turn.

### Advantages

- Simple control flow.
- Easy to debug.
- Useful for demos, learning, and scripts.

### Limitations

- Blocks while waiting for model events.
- Does not handle multiple conversations at once.
- Is less suitable for high-concurrency services.

## Asynchronous Chat Application (`chat-async.py`)

```text
User Input
    |
Async Event Loop
    |
AsyncOpenAI Client
    |
Async Responses API Request
    |
Azure OpenAI Model
    |
Async Streaming Events
    |-- response.output_text.delta -> Display text chunk
    `-- response.completed -> Save response ID
    |
Next Turn Uses previous_response_id
```

### Flow

1. The user enters a prompt.
2. The event loop awaits an async Responses API request.
3. The model streams events back through an async iterator.
4. The app prints each text delta immediately.
5. The app stores the completed response ID for the next turn.

### Advantages

- Non-blocking I/O model.
- Fits naturally into async Python services.
- Better foundation for concurrent chat sessions.

### Use Cases

- FastAPI or Starlette applications.
- WebSocket chat servers.
- Event-driven services.
- API servers handling many clients.

## Responses API vs Chat Completions

| Feature | Chat Completions | Responses API |
| --- | --- | --- |
| Message format | Array of messages | Direct input and instructions |
| Conversation tracking | Manual history management | Response ID linking |
| Streaming | Supported | Supported |
| Tool support | Function calling | Native tool support |
| Syntax | More verbose | More direct |
| Learning curve | Steeper | Gentler |

## Conversation Context Management

The scripts use response IDs instead of storing a local message history.

```text
Exchange 1:
  User: "Tell me about ELIZA"
  Response ID: abc123

Exchange 2:
  User: "How does it compare to modern LLMs?"
  previous_response_id: abc123

The model can use the previous response context and understand that "it" refers to ELIZA.
```

### Benefits

- Less local state to manage.
- Cleaner prompt construction.
- Efficient context linking through the API.

## Technology Stack

- **Language:** Python 3.13+
- **SDK:** OpenAI Python SDK
- **Authentication:** Azure Identity
- **Model:** Azure OpenAI model deployment
- **Infrastructure:** Microsoft Foundry / Azure OpenAI Service
- **Concurrency:** `asyncio` for the async implementation

## Error Handling and Resilience

Implemented:

- Azure credential authentication with `DefaultAzureCredential`.
- Environment variable validation.
- Graceful terminal error output.
- Credential cleanup in `finally` blocks.

Recommended for production:

- Retry logic with exponential backoff.
- Rate limit handling.
- Structured logging.
- Health checks.
- Centralized configuration management.

## Deployment Considerations

### Synchronous App

- Good for standalone scripts.
- Good for learning and demos.
- Best when only one request is handled at a time.

### Asynchronous App

- Better for web APIs and services.
- Easier to adapt for concurrent sessions.
- Better fit for cloud-native Python applications.

## Performance Characteristics

### Streaming Benefits

- Lower time to first visible text.
- More responsive user experience.
- Processes chunks as they arrive.

### Async Benefits

- Avoids blocking during network I/O.
- Allows other async work to run while waiting.
- Scales better in services that manage many connections.
