from querychat import QueryChat
from querychat.data import titanic
import shiny.express

qc = QueryChat(
    titanic(),
    "titanic",
    client="bedrock-anthropic",
    tools=("filter", "query", "visualize"),
)

app = qc.app()
