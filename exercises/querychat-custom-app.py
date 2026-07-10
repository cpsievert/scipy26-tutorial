"""
querychat exercise: build a self-service analytics app
=======================================================

This starter gives you a working querychat app on the Titanic dataset.
Work through as many tasks as you can:

  1. SWAP YOUR DATA: Replace the Titanic dataset with your own CSV
     (or try one of these):
       - seaborn tips: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
       - Palmer penguins: https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv
     Add a data_description to help the LLM understand your columns.

  2. ADD WEB SEARCH: Register tool_web_search() so the assistant can
     answer questions beyond the dataset.

  3. ADD A CUSTOM TOOL: Write a tool that does something the built-in
     tools can't (e.g., export filtered data to CSV).

Run with:  shiny run querychat-custom-app.py
"""

import polars as pl
from shiny.express import render, ui
from querychat.express import QueryChat
from querychat.data import titanic

# -------------------------------------------------------------------
# Task 1: swap this for your own data
# e.g., pl.read_csv("your_data.csv")
# -------------------------------------------------------------------
data = titanic()

qc = QueryChat(
    data,
    "titanic",
    # Task 1: add a data_description for your data, e.g.:
    # data_description="survived: 1 = survived, 0 = did not survive",
)

# -------------------------------------------------------------------
# Task 2: add web search
# -------------------------------------------------------------------
# from chatlas import tool_web_search
# qc.client().register_tool(tool_web_search())

# -------------------------------------------------------------------
# Task 3: add a custom tool — here's a skeleton
# -------------------------------------------------------------------
# def export_to_csv(filename: str):
#     """Export the current filtered data to a CSV file.
#
#     Parameters
#     ----------
#     filename
#         The name of the CSV file to create (e.g., "filtered_data.csv").
#     """
#     qc.df().to_csv(filename, index=False)
#     return f"Exported {len(qc.df())} rows to {filename}"
#
# qc.client().register_tool(export_to_csv)

# -------------------------------------------------------------------
# App layout
# -------------------------------------------------------------------
qc.sidebar()

with ui.card():
    with ui.card_header():

        @render.text
        def title():
            return qc.title() or "Titanic Dataset"

    @render.data_frame
    def data_table():
        return qc.df()

ui.page_opts(fillable=True, title="Titanic Explorer")
