"""
Example: Tool use with Anthropic Claude
"""

from anthropic import Anthropic

client = Anthropic(api_key="your-api-key")

tools = [{
    "name": "get_weather",
    "description": "Get weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        }
    }
}]

response = client.messages.create(
    model="claude-3-opus-20240229",
    messages=[{"role": "user", "content": "What's the weather in SF?"}],
    tools=tools
)

print(response)

