"""
Yandex Search API MCP Server

This module implements an MCP server providing access to Yandex Search API v2 features:
- Web search (preferred endpoint)
- AI-powered search (expensive endpoint)

Copyright © 2025 Yandex LLC. Licensed under Apache License 2.0.

Features:
- FastMCP integration
- Input validation
- Error handling
- Configuration via environment variables
"""

import json
import xml.etree.ElementTree as ET
import os
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP
from detail import validate_input_data, call_ai_search_with_yazeka, call_web_search

# Create an MCP server
mcp = FastMCP(
    name="Yandex Search Api v2, web and generation"
)


@mcp.tool()
def ai_search_with_yazeka(body: dict) -> str:
    """
    Use this tool when the user needs to search online, the search query is complex, and a short summary of the web search results 
    will make the answer easier to understand. Always call this tool if the user explicitely asks to search with yazeka.

    Args:
        body (dict): Required. input containing:
            - query: Required. search query string. Can contain a question and keywords
            - search_region: Required. Search region. Valid values: 'tr' - Turkish region, 'en' - English region

        minimal example: "body": {
                                "query": "Who won the most recent Formula 1 race in 2025?",
                                "search_region": "tr"
                         }

    Returns:
        dict: array of data and source
    """
    data = body
    required_keys = {"query", "search_region"}
    if error_message := validate_input_data(data, required_keys):
        return error_message

    api_response = json.loads(call_ai_search_with_yazeka(data)[1:-1])
    response = dict()
    response["response"] = api_response["message"]["content"]
    response["sources"] = [source["url"] for source in api_response["sources"] if source["used"]]

    return json.dumps(response, ensure_ascii=False, indent=2)


@mcp.tool()
def web_search(body: dict) -> str:
    """
    Use this tool when the user needs to search online and the search query is simple.

    Args:
        body (dict): Required. input containing:
            - query: Required. search query string. Can contain a question and keywords
            - search_region: Required. Search region. Valid values: 'tr' - Turkish region, 'en' - English region

        minimal example:    "body": {
                                "query": "who won the latest F1 race 2025",
                                "search_region": "tr"
                            }

    Returns:
        dict: array of data and source

    Note:
        Default to Turkish localization/region/domain unless query is explicitly non-Turkish.
    """
    data = body
    required_keys = {"query", "search_region"}
    if error_message := validate_input_data(data, required_keys):
        return error_message

    root = ET.fromstring(call_web_search(data))

    response = {'responses': []}
    for doc in root.iter('doc'):
        response["responses"].append({'data': doc.find("./properties/extended-text").text, 'source': doc.find("url").text})
    
    return json.dumps(response, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        raise
