
# Architecture Overview

---

## Synchronous Chat Application (`chat-app.py`)

```text
User Input
    ↓
Azure OpenAI Client
    ↓
Responses API Request
    ↓
Azure OpenAI Model (GPT-4.1)
    ↓
Streaming Response Events
    ├─ response.output_text.delta → Display chunks
    └─ response.completed → Save response ID
    ↓
User Display + Context Storage
```

**Key Flow:**

1. User enters prompt
2. Client sends synchronous request
3. Model processes and streams response
4. Each chunk displays immediately
5. Response ID saved for context linking

**Advantages:**

- Simpler control flow
- Easier to debug
- Straightforward error handling

**Limitations:**

- Blocks execution while waiting
- Can't handle concurrent requests
- Not suitable for high-concurrency scenarios

---

## Asynchronous Chat Application (`chat-async.py`)

```text
User Input
    ↓
Async Event Loop
    ↓
AsyncOpenAI Client
    ↓
Async Responses API Request
    ↓
Azure OpenAI Model (GPT-4.1)
    ↓
Awaitable Response
    ├─ Non-blocking wait
    └─ Event loop can handle other tasks
    ↓
Response Processing + Context Storage
```

**Key Flow:**

1. User enters prompt
2. Event loop executes async request
3. `await` pauses execution without blocking
4. Other tasks can execute simultaneously
5. Response ID saved when complete

**Advantages:**

- Non-blocking architecture
- Handles concurrent operations
- Better resource utilization
- Production-ready for APIs

**Use Cases:**

- Web APIs (FastAPI, Flask-Async)
- High-concurrency services
- Event-driven applications
- Server handling multiple clients

---

## Responses API vs ChatCompletions

| Feature               | ChatCompletions      | Responses API                |
|----------------------|---------------------|------------------------------|
| Message Format       | Array of messages   | Direct instructions          |
| Conversation Tracking| Manual management   | Built-in (response IDs)      |
| Streaming            | Yes                | Yes                         |
| Tool Support         | Via function_calling| Native (in tools-augmented)  |
| Syntax               | Verbose            | Simple                      |
| Learning Curve       | Steeper            | Gentler                     |

---

## Conversation Context Management

**How Response IDs Work:**

```text
Exchange 1:
  User: "Tell me about ELIZA"
  Response ID: abc123

Exchange 2:
  User: "How does it compare to modern LLMs?"
  previous_response_id: abc123 ← Links back

  Model receives:
  1. User's current question
  2. Previous response context (from ID)
  3. Can understand "it" refers to ELIZA
```

**Benefits:**

- Automatic context management
- No need to store message history
- Efficient token usage
- Clean API design

---

## Technology Stack

- **Language:** Python 3.13+
- **SDK:** OpenAI Python SDK v2.33+
- **Authentication:** Azure Identity (token-based)
- **Model:** Azure OpenAI GPT-4.1
- **Infrastructure:** Microsoft Foundry / Azure OpenAI Service
- **Concurrency:** asyncio (Python standard library)

---

## Error Handling & Resilience

**Implemented:**

- Credential authentication with DefaultAzureCredential
- Graceful error reporting
- Resource cleanup in finally blocks
- Input validation

**For Production:**

- Retry logic with exponential backoff
- Rate limiting handling
- Comprehensive logging
- Health checks
- Circuit breakers

---

## Deployment Considerations

**Synchronous (`chat-app.py`):**

- Simple standalone scripts
- Scheduled jobs
- Sequential processing
- Learning/demo purposes

**Asynchronous (`chat-async.py`):**

- FastAPI/Starlette applications
- gRPC services
- WebSocket servers
- High-throughput APIs
- Cloud-native deployments

---

## Performance Characteristics

**Streaming Benefits:**

- Time-to-first-token: Minimal latency
- User perception: Responsive interface
- Memory efficiency: Process chunks vs entire response
- Network optimization: Progressive delivery

**Async Benefits:**

- Throughput: Handle 100s of concurrent requests
- Latency: Non-blocking during I/O
- Resource usage: Minimal thread overhead
- Scalability: Efficient resource pooling
