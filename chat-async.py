import asyncio
import os

from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import AsyncOpenAI


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


async def main() -> None:
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")
    credential = None

    try:
        # Get configuration settings
        load_dotenv()
        azure_openai_endpoint = get_required_env("AZURE_OPENAI_ENDPOINT")
        model_deployment = get_required_env("MODEL_DEPLOYMENT")

        # Initialize an async OpenAI client
        credential = DefaultAzureCredential()
        token_provider = get_bearer_token_provider(
            credential, "https://ai.azure.com/.default"
        )

        async_client = AsyncOpenAI(base_url=azure_openai_endpoint, api_key=token_provider)

        # Track responses
        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # Stream an asynchronous response
            stream = await async_client.responses.create(
                model=model_deployment,
                instructions="You are a helpful AI assistant that answers questions and provides information.",
                input=input_text,
                previous_response_id=last_response_id,
                stream=True,
            )
            print("Assistant: ", end="", flush=True)
            async for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                elif event.type == "response.completed":
                    last_response_id = event.response.id
            print()

    except Exception as ex:
        print(ex)

    finally:
        # Close the async client session
        if credential is not None:
            await credential.close()


if __name__ == "__main__":
    asyncio.run(main())
