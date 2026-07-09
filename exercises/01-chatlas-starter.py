import uuid

import ipywidgets
import requests
import chatlas as ctl
from chatlas import ContentToolResult
from ipyleaflet import CircleMarker, Map
from shinychat.types import ToolResultDisplay
from shinywidgets import output_widget, register_widget


def get_current_weather(latitude: float, longitude: float, location_name: str):
    """Get the current temperature given a latitude and longitude."""

    lat_lng = f"latitude={latitude}&longitude={longitude}"
    url = f"https://api.open-meteo.com/v1/forecast?{lat_lng}&current=temperature_2m,wind_speed_10m"
    response = requests.get(url)
    json = response.json()
    current = json["current"]

    loc = (latitude, longitude)
    info = (
        f"<h6>Current weather</h6>"
        f"Temperature: {current['temperature_2m']}°C<br>"
        f"Wind: {current['wind_speed_10m']} m/s<br>"
        f"Time: {current['time']}"
    )

    m = Map(center=loc, zoom=10)
    m.add_layer(CircleMarker(location=loc, popup=ipywidgets.HTML(info)))

    widget_id = f"weather_{uuid.uuid4().hex}"
    register_widget(widget_id, m)

    return ContentToolResult(
        value=current,
        extra={
            "display": ToolResultDisplay(
                html=output_widget(widget_id),
                title=f"Weather for {location_name}",
                show_request=False,
                open=True,
                full_screen=True,
            )
        },
    )


# TODO(1): add a system_prompt argument here
chat = ctl.ChatBedrockAnthropic()

chat.register_tool(get_current_weather)
# TODO(2): register your second tool here
# TODO(3): register tool_web_search() here

chat.app()
