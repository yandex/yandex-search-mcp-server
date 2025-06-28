# Yandex Search MCP Server 🔍

This Model Context Protocol (MCP) server lets AI assistants like Claude and Cursor use the Yandex Search API for searching the web. Yandex Search enables LLM agents to safely and easily find up-to-date information on the internet.

## Yandex Search Remote MCP

Connect directly to Yandex's hosted MCP server (no need to run it locally).

### Yandex Search MCP URL for Remote Connection

```
https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse
```

### Available Tools

The Yandex Search MCP server includes the following tools:

- **search-api_post**: Performs a real-time web search and returns an encoded XML of the search results page

## How to Add Yandex Search MCP to Claude Desktop 🤖

### 1. Configure Claude Desktop to Recognize MCP Servers

Open the Claude Desktop app and enable Developer Mode from the top-left menu bar.

Once enabled, open Settings (also from the top-left menu bar) and navigate to the Developer Option.

Click the Edit Config button to open the claude_desktop_config.json file

### 2. Add Yandex Search MCP to Claude Desktop

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
      ]
    }
  }
}
```

### 3. Restart Claude Desktop

For the changes to take effect:

1. Completely quit Claude Desktop (not just close the window)
2. Start Claude Desktop again
3. Click "Search and Tools" to verify that yandexSearch is enabled and running

## How to Add Yandex Search MCP to Cursor 🤖

### 1. Configure Cursor to Recognize MCP Servers

Open Settings and navigate to Tools and Integrations in the left panel.

Click the Add Custom MCP button to create the mcp.json config file in cursor

### 2. Add Yandex Search MCP to Cursor

Add the following text to your Claude Desktop configuration file:

```json
{
  "servers": {
    "yandexSearch": {
      "type": "sse",
      "url": "https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse"
    }
  }
}
```

### 3. Find information on the web with yandexSearch

1. Verify the setup by typing the following text in the chat:
```
use yandexSearch to find information about the best AI Agent frameworks in 2025
```
2. Cursor will ask you to confirm that it should use yandexSearch, click the Run Tool button or press (⌘↵) to confirm.
3. You should see "called search-api_post" in the chat and the answer based on the web search results.

## How to Add Yandex Search MCP to Visual Studio Code 🤖

### 1. Configure Visual Studio Code to Recognize MCP Servers

Enable the [chat.mcp.enabled](vscode://settings/chat.mcp.enabled) setting in VS Code to enable MCP support.

Add a .vscode/mcp.json file in your workspace to configure MCP servers for a workspace.

### 2. Add Yandex Search MCP to Visual Studio Code

Add the following text to your Claude Desktop configuration file:

```json
{
  "servers": {
    "yandexSearch": {
      "type": "sse",
      "url": "https://d5dj4o5pbnqgca1d546v.cmxivbes.apigw.yandexcloud.net:3000/sse"
    }
  }
}
```

### 3. Open CoPilot in Agent Mode

1. Open the Chat view (⌃⌘I), and select Agent mode from the dropdown.
2. Select the Tools button to view the list of available tools.
3. The AI Agent will automatically select yandexSearch when it needs to find information on the internet.
4. To ensure that the AI Agent uses yandexSearch click the Add Context Button, and select search-api_post from the available tools.
5. For advanced configuration settings visit [the official VS Code MCP tutorial](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

<br>

---

Built by the Yandex team with ❤️
