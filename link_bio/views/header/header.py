import reflex as rx

def header() -> rx.Component: # funcion que devuelve un componente de reflex
    return rx.vstack(
        rx.avatar(fallback="NM"),
        rx.text("Mi nombre es Nicolás Llanos soy ingeniero informatica hace 10 años, me especializo en ingenieria de datos en big data y autodidacta en aplicaciones web")
    )