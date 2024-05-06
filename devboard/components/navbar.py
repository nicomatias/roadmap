import reflex as rx

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