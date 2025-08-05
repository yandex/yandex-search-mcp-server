# Yandex Search MCP Server

This Model Context Protocol (MCP) server lets AI assistants like Claude and Cursor use the Yandex Search API for searching the web. Yandex Search enables LLM agents to safely and easily find up-to-date information on the internet.

## Available Tools

The Yandex Search MCP server includes the following tools:

- **ai_search_post** Performs a real-time web search and returns an AI-generated answer based on the search results using Yandex Yazeka AI model. 
- **web_search_post**: Performs a real-time web search and returns answer with sources

## Getting API Key

To use this MCP server, you need to be a customer of Yandex Search API. You need a Yandex Search API key:
- [API Key Documentation](https://yandex.cloud/ru/docs/search-api/api-ref/authentication)

### Yandex Search MCP URL for Remote Connection

```
https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse
```

## How to use Yandex Search MCP Remotely (recommended)
### How to Add Yandex Search MCP to Claude 🤖

#### 1. Configure Claude Desktop to Recognize MCP Servers

Open the Claude Desktop app and enable Developer Mode from the top-left menu bar.

Once enabled, open Settings (also from the top-left menu bar) and navigate to the Developer Option.

Click the Edit Config button to open the claude_desktop_config.json file

#### 2. Add Yandex Search MCP to Claude Desktop

Add the following text to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "yandexSearch": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse"
      ],
      "headers": {
        "ApiKey": "<your_api_key>"
      }
    }
  }
}
```

#### 3. Restart Claude Desktop

For the changes to take effect:

1. Completely quit Claude Desktop (not just close the window)
2. Start Claude Desktop again
3. Click "Search and Tools" to verify that yandexSearch is enabled and running

### How to Add Yandex Search MCP to Cursor 🤖

#### 1. Configure Cursor to Recognize MCP Servers

Open Settings and navigate to Tools and Integrations in the left panel.

Click the Add Custom MCP button to create the mcp.json config file in cursor

#### 2. Add Yandex Search MCP to Cursor

Add the following text to your Claude Desktop configuration file:

```json
{
  "servers": {
    "yandexSearch": {
      "type": "sse",
      "url": "https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse",
      "headers": {
        "ApiKey": "<your_api_key>"
      }
    }
  }
}
```

#### 3. Find information on the web with yandexSearch

1. Verify the setup by typing the following text in the chat:
```
use yandexSearch to find information about the best AI Agent frameworks in 2025
```
2. Cursor will ask you to confirm that it should use yandexSearch, click the Run Tool button or press (⌘↵) to confirm.
3. You should see "called search-api_post" in the chat and the answer based on the web search results.

### How to Add Yandex Search MCP to Visual Studio Code 🤖

#### 1. Configure Visual Studio Code to Recognize MCP Servers

Enable the [chat.mcp.enabled](vscode://settings/chat.mcp.enabled) setting in VS Code to enable MCP support.

Add a .vscode/mcp.json file in your workspace to configure MCP servers for a workspace.

#### 2. Add Yandex Search MCP to Visual Studio Code

Add the following text to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "yandexSearch": {
      "type": "sse",
      "url": "https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse",
      "headers": {
        "ApiKey": "<your_api_key>"
      }
    }
  }
}
```

#### 3. Open CoPilot in Agent Mode

1. Open the Chat view (⌃⌘I), and select Agent mode from the dropdown.
2. Select the Tools button to view the list of available tools.
3. The AI Agent will automatically select yandexSearch when it needs to find information on the internet.
4. To ensure that the AI Agent uses yandexSearch click the Add Context Button, and select search-api_post from the available tools.
5. For advanced configuration settings visit [the official VS Code MCP tutorial](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## How to run Yandex Search MCP locally

### Prerequisites

- Python 3.10+
- Node.js 16+ (for MCP development)
- Docker 20+ or Podman 3+ (for containerized deployment)

### Installation

```bash
git clone git@github.com:yandex/yandex-search-mcp-server.git
cd /path/to/yandex-search-mcp-server
```
### Option 1: Use Yandex Search MCP with Docker/Podman

To run the MCP server in a container using Docker or Podman:

1. Ensure Docker and Docker Compose, or Podman and Podman Compose, are installed on your system.
2. For Podman users: If you need to pull images from Docker Hub, first authenticate:
   ```bash
   podman login docker.io
   ```
   Enter your Docker Hub username and password when prompted.
3. Build the container:
   - Using Docker:
     ```bash
     docker build -t yandex-mcp-server-image:latest .
     ```
   - Using Podman:
     ```bash
     podman build -t yandex-mcp-server-image:latest .
     ```

This will create an image named `yandex-mcp-server-image`.

You need to add MCP server configs and set `SEARCH_API_KEY`.

For container deployment, if your MCP system supports direct interaction with Docker or Podman containers, you might use configurations like these (adjust based on your MCP system's requirements):

- Using Docker:
```json
{
  "mcpServers": {
    "yandex-search-api-docker": {
      "autoApprove": [],
      "disabled": true,
      "timeout": 60,
      "type": "stdio",
      "command": "sh",
      "args": [
        "-c",
        "docker rm -f yandex-mcp-container; docker run -i --name yandex-mcp-container --env SEARCH_API_KEY=<your_api_key> yandex-mcp-server-image:latest"
      ]
    }
  }
}
```

- Using Podman:
```json
{
  "mcpServers": {
    "yandex-search-api-podman": {
      "autoApprove": [],
      "disabled": true,
      "timeout": 60,
      "type": "stdio",
      "command": "sh",
      "args": [
        "-c",
        "podman rm -f yandex-mcp-container; podman run -i --name yandex-mcp-container --env SEARCH_API_KEY=<your_api_key> yandex-mcp-server-image:latest"
      ]
    }
  }
}
```

**Important**: Replace `<your_api_key>` with your actual Yandex Search API key. Ensure that only one instance of the server (local or Docker) is active at a time to avoid conflicts.

After updating the configuration, the system should automatically detect and run the server, exposing the `ai_search_with_yazeka` and `web_search` tools for use.

### Option 2: Use Python + MCP Config

#### Step 1. Install required libraries

```bash
  pip install -r requirements.txt
```

#### Step 2. Configure the MCP Settings for Local Python Execution

To setup the MCP server on your system using Python, add the following configuration to your MCP settings and set `SEARCH_API_KEY`:

```json
{
  "mcpServers": {
    "yandex-search-api": {
      "autoApprove": [],
      "disabled": true,
      "timeout": 60,
      "type": "stdio",
      "command": "env",
      "args": [
        "SEARCH_API_KEY=<your_api_key>",
        "python3",
        "/path/to/mcp-server-demo/server.py"
      ]
    }
  }
}
```

**Important**: Replace `<your_api_key>` with your actual Yandex Search API key and update `/path/to/mcp-server-demo` to the actual path where the repository is located on your system if necessary.

After updating the configuration, the system should automatically detect and run the server, exposing the `ai_search_with_yazeka` and `web_search` tools for use.

#### Step 3. Launch the local MCP Server

To run the MCP server directly on your machine without containerization:

1. Ensure you have Python 3.10+ installed.
2. Set the required environment variable for the API key (replace `<your_api_key>` with your actual Yandex Search API key):
```bash
export SEARCH_API_KEY=<your_api_key>
```
3. Run the server:
```bash
python3 server.py
```

The server will start and listen for input on stdin, responding on stdout. Typically, this server is integrated with a system that communicates via MCP.

### Example Requests

#### Web Search Example
```json
{
    "query": "Who won the most recent Formula 1 race in 2025?",
    "search_region": "en"
}
```

#### AI Search Example
```json
{
    "query": "Who won the most recent Formula 1 race in 2025?",
    "search_region": "en"
}
```

## Troubleshooting

- If the server fails to start, ensure all dependencies are installed correctly (`pip install -r requirements.txt`).
- If you encounter authentication errors, double-check that the `SEARCH_API_KEY` is correctly set in your environment or configuration.

<br>

---

Built by the Yandex team with ❤️
