from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("mcp-poc-server")

@app.tool()
def hello(name: str) -> str:
    return f"Hello {name}, welcome to MCP 🎉"

if __name__ == "__main__":
    stdio_server(app)