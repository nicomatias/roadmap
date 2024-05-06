import reflex as rx
from componentes.barra_navegacion import barra_navegacion
from views.header.header import header
# para el proyecto devboard piensa en utilizar cards dentro de boxes dentro de un vstack de dos hstacks los cuales llamaran a scripts js

class State(rx.State): # estados de clicks
    pass

def index() -> rx.Component: # funcion que devuelve un componente de reflex
    return rx.vstack(
        barra_navegacion(),
        header()
    )
    # return rx.text("Hola Reflex!",color="blue") # devolvemos el texto de reflex y con propiedades de css

app = rx.App() # app va a ser la variable que contiene una aplicacion de reflex
app.add_page(index) # añadimos la pagina index a reflex, aca se podrian añadir muchisimas
app.compile() # compilamos la app