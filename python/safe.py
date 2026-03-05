# test_mcp.py
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient(
        connections={
            "time": {
                "transport": "stdio",
                "command": r"C:\Users\SunnyBharti\Downloads\lca-langchainV1-essentials\python\mcp_tools\mcp-time.windows-amd64.exe",  
                "args": [],                       # empty list – binary needs no args
            }
        }
    )
    tools = await client.get_tools()
    return tools
    #print(f"Loaded {len(tools)} tools: {[t.name for t in tools]}")
    
if __name__ == "__main__":
    asyncio.run(main())
