"""
chatlas exercise: build a tool-using chat
==========================================

This starter gives you a working chatlas chat with one tool.
Your tasks:

  1. Add a system prompt that gives the assistant a persona
     (e.g., a pirate, a data science tutor, a cooking assistant)

  2. Register a second tool — ideas:
     - A dice roller: roll_dice(sides: int, count: int)
     - A unit converter: convert_temperature(value: float, from_unit: str, to_unit: str)
     - A dataset summarizer: describe your own CSV

  3. BONUS: add web search
     from chatlas import tool_web_search
     chat.register_tool(tool_web_search())

Run with:  python 01-chatlas-starter.py
"""

import chatlas as ctl


def get_current_weather(lat: float, lng: float):
    """Get the current weather for a location.

    Parameters
    ----------
    lat
        The latitude.
    lng
        The longitude.
    """
    import requests

    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lng, "current": "temperature_2m"},
    )
    return resp.json()["current"]


# TODO(1): add a system_prompt argument here
chat = ctl.ChatBedrockAnthropic()

chat.register_tool(get_current_weather)
# TODO(2): register your second tool here
# TODO(3): register tool_web_search() here

chat.console()
