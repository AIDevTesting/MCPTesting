import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def main():
    async with streamablehttp_client("http://127.0.0.1:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call your 'add' tool
            result = await session.call_tool("add", {"a": 10, "b": 20})
            print("add result:", result)

            # Call your 'hello' tool
            result = await session.call_tool("hello", {"name": "Amit"})
            print("hello result:", result)

            # Call your prompt 'greet_user' (if you have one)
            result = await session.call_tool("greet_user", {"name": "Amit", "style": "friendly"})
            print("greet_user result:", result)

if __name__ == "__main__":
    asyncio.run(main())
