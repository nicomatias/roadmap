// funciones.js

var myArray = [1, 2, 3];

function Print() {
    // var myArray = [1, 2, 3];
    var contenido = document.getElementById('contenido');
    contenido.innerHTML = myArray; // Añade una línea nueva al contenido
}

function AddEnd() {
    myArray.push("Final");
    var contenido = document.getElementById('contenido');
    contenido.innerHTML = myArray; // Añade una línea nueva al contenido
}

function AddFirst() {
    myArray[0] = "Inicio"; 
    var contenido = document.getElementById('contenido');
    contenido.innerHTML = myArray; // Añade una línea nueva al contenido
}
