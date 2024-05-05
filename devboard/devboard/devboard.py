"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


# def index() -> rx.Component:
#     return rx.center(
#         # rx.theme_panel(),
#         rx.vstack(
#             rx.heading("Dev Dashboard", size="9"),
#             rx.text("Get started by editing ", rx.code(filename)),
#             rx.button(
#                 "Check out our docs!",
#                 on_click=lambda: rx.redirect(docs_url),
#                 size="4",
#             ),
#             rx.logo(),
#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )

def content():
    # return rx.box(
    #     rx.heading("Developer Dashboard"),
    #     rx.text("This is the main content of the page."),
    # )

    return rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Pomodoro"),
            rx.table.column_header_cell("To-do list"),
            rx.table.column_header_cell("Note Taking"),
            rx.table.column_header_cell("Stand Up Reminder"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell("Danilo Sousa"),
            rx.table.cell("danilo@example.com"),
            rx.table.cell("Developer"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Zahra Ambessa"),
            rx.table.cell("zahra@example.com"),
            rx.table.cell("Admin"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Jasper Eriksson"),
            rx.table.cell("jasper@example.com"),
            rx.table.cell("Developer"),
        ),
    ),
    )


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.jpg", width="2em"),
            rx.heading("Developer Dashboard - Devboard", font_size="2em"),
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
            ),
            rx.menu.content(
                rx.menu.item("Set Light or Dark"),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )


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
