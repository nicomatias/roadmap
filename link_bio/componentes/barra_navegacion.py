import reflex as rx

def barra_navegacion() -> rx.Component: # funcion que devuelve un componente de reflex
    return rx.hstack(
        rx.text("Nico Matias Link Tree",
        height="40px"
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999"  
    )