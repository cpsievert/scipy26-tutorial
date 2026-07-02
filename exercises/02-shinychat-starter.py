"""
shinychat exercise: build a chatbot with custom tool displays
==============================================================

This starter gives you a working shinychat app with a weather tool.
Your tasks:

  1. Run the app:  shiny run 02-shinychat-starter.py
     Ask it about the weather somewhere. Notice the default tool display.

  2. Upgrade the tool to return a ToolResultDisplay:
     - Import ContentToolResult from chatlas
     - Import ToolResultDisplay from shinychat.types
     - Return a ContentToolResult with a display in the extra dict

  3. BONUS: add a slash command
     @chat.slash_command("clear", "Clear the chat")
     async def _():
         await chat.clear_messages()

Run with:  shiny run 02-shinychat-starter.py
"""

import chatlas as ctl
from shiny.express import ui
from shinychat.express import Chat

ui.page_opts(title="Weather Chatbot", fillable=True)


def get_weather(lat: float, lng: float, location: str):
    """Get the current weather for a location.

    Parameters
    ----------
    lat
        The latitude.
    lng
        The longitude.
    location
        A human-readable name for the location (e.g., "Paris, France").
    """
    import requests

    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lng,
            "current": "temperature_2m,wind_speed_10m",
        },
    )
    data = resp.json()["current"]
    return data

    # TODO(2): instead of returning `data` directly, return a ContentToolResult:
    #
    # from chatlas import ContentToolResult
    # from shinychat.types import ToolResultDisplay
    #
    # return ContentToolResult(
    #     value=data,
    #     extra={
    #         "display": ToolResultDisplay(
    #             title=f"Weather: {location}",
    #             markdown=f"**{data['temperature_2m']}°C** · Wind: {data['wind_speed_10m']} km/h",
    #         )
    #     },
    # )


client = ctl.ChatAnthropic(
    system_prompt="You are a helpful weather assistant. Use the weather tool to answer questions.",
)
client.register_tool(get_weather)

chat = Chat(id="chat", client=client)
chat.ui(
    messages=["Hi! Ask me about the weather anywhere in the world."],
    placeholder="e.g., What's the weather in Tokyo?",
)

# TODO(3): add a slash command to clear the chat
# @chat.slash_command("clear", "Clear the conversation")
# async def _():
#     await chat.clear_messages()
