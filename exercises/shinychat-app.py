import chatlas as ctl
import requests
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
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lng,
            "current": "temperature_2m,wind_speed_10m",
        },
    )
    return resp.json()["current"]


client = ctl.ChatBedrockAnthropic(
    system_prompt="You are a helpful weather assistant. Use the weather tool to answer questions.",
)
client.register_tool(get_weather)

chat = Chat(id="chat", client=client)
chat.ui(
    messages=["Hi! Ask me about the weather anywhere in the world."],
    placeholder="e.g., What's the weather in Tokyo?",
)
