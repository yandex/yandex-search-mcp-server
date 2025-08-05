import os
import json
import base64
from typing import Dict, Any, Optional, Union

import requests
from requests.exceptions import RequestException

# API Configuration
GEN_SEARCH_URL = "https://searchapi.api.cloud.yandex.net/v2/gen/search"
WEB_SEARCH_URL = "https://searchapi.api.cloud.yandex.net/v2/web/search"
DEFAULT_TIMEOUT = 30


def make_http_request(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = DEFAULT_TIMEOUT,
    decode_base64: bool = False
) -> str:
    try:
        with requests.post(url, headers=headers, json=json_body, timeout=timeout) as response:
            response.raise_for_status()
            
            if decode_base64:
                decoded_data = base64.b64decode(json.loads(response.text)["rawData"]).decode('utf-8')
                return decoded_data
            return response.text
                
    except RequestException as e:
        raise RuntimeError(f"API request failed: {str(e)}") from e


def validate_input_data(data: Dict[str, Any], required_keys: set) -> Optional[str]:
    if missing_keys := required_keys - set(data):
        return f"Missing required keys: {', '.join(missing_keys)}"
    return None


def call_ai_search_with_yazeka(data: Dict[str, Any]) -> str:
    api_key = os.getenv('SEARCH_API_KEY')
    if not api_key:
        raise ValueError("SEARCH_API_KEY environment variable not set")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {api_key}"
    }
    body = {
        "messages": [{"content": data["query"], "role": "ROLE_USER" }],
        "searchFilters": [ { "lang": ("tr" if data["search_region"] == 'tr' else "en")} ],
        "folderId": "b1gudsjclvkga651dgci",
        "fixMisspell": True,
        "enableNrfmDocs": True,
        "search_type": "SEARCH_TYPE_TR" if data["search_region"] == 'tr' else "SEARCH_TYPE_COM"
    }
    return make_http_request(GEN_SEARCH_URL, headers=headers, json_body=body, timeout=200)


def call_web_search(data: Dict[str, Any]) -> str:
    api_key = os.getenv('SEARCH_API_KEY')
    if not api_key:
        raise ValueError("SEARCH_API_KEY environment variable not set")

    headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Api-Key {api_key}"
    }

    body = {
        "query": {
            "searchType": "SEARCH_TYPE_TR" if data["search_region"] == 'tr' else "SEARCH_TYPE_COM",
            "queryText": data["query"],
            "familyMode": "FAMILY_MODE_NONE",
            "fixTypoMode": "FIX_TYPO_MODE_OFF",
        },
        "groupSpec": {"groupsOnPage": 4},
        "l10n": "LOCALIZATION_TR" if data["search_region"] == 'tr' else "LOCALIZATION_EN",
        "region": data["search_region"],
        "responseFormat": "FORMAT_XML"
    }

    return make_http_request(WEB_SEARCH_URL, headers=headers, json_body=body, timeout=10, decode_base64=True)
