from querychat import QueryChat
from querychat.data import titanic
import shiny

qc = QueryChat(
    titanic(),
    "titanic",
    client="anthropic",
    tools=("filter", "query", "visualize"),
)

app = qc.app()
