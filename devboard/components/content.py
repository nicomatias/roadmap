import reflex as rx

def content():
    return rx.flex(
    rx.card("Card 1"),
    rx.card("Card 2"),
    rx.card("Card 3"),
    rx.card("Card 4"),
    spacing="2",
    width="100%",
)