"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

from components.navbar import navbar
from components.content import content

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

# def index() -> rx.Component:

def index():
    return rx.fragment(
        navbar(),
        rx.container(
            content(),
            padding_top="6em",
            max_width="60em",
        ),
    )


app = rx.App()
app.add_page(index)
