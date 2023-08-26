var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apiconsultar = "ListaCurso.php";
var apieliminar = "BorrarCursos.php";
var apieditar = "ActualizarCursos.php";

const myModalEliminar = new bootstrap.Modal(document.getElementById('myModalEliminar')); 
const myModalEditar = new bootstrap.Modal(document.getElementById('myModalEditar'));
const modalSuccess = new bootstrap.Modal(document.getElementById('modalSuccess'));

let tablaresultado = document.querySelector('#tablaresultado');

function consultardatos(){
    //fetch sirve para extraer, insertar modificar, eliminar consultardatos, 
    apiurl = apibase + apiconsultar ;
    fetch(apiurl)
    .then(estructura => estructura.json())
    .then((datosrespuesta) => {
            //ajustardatostabla
            console.log(datosrespuesta.code) 
            console.log(datosrespuesta.data) 
            ajustardatostabla(datosrespuesta.data) 
        })
    .catch(console.log);
}

function ajustardatostabla(datos){
    console.log("datos"+datos);
    for (const objetoindividual of datos) {

       tablaresultado.innerHTML += `
            <tr class="table-primary" >
                                <td scope="row">${objetoindividual.id}</td>
                                <td>${objetoindividual.nombre}</td>
                                <td>${objetoindividual.descripcion}</td>
                                <td>${objetoindividual.tiempo}</td>
                                <td>${objetoindividual.usuario}</td>
                                <td>
                                <a name="Editar" id="Editar" class="btn btn-success" role="button" onclick="mostrarEditarModal('${objetoindividual.id}','${objetoindividual.nombre}','${objetoindividual.descripcion}','${objetoindividual.tiempo}')"> Editar </a> 
                                ||
                                <a name="Eliminar" id="Eliminar" class="btn btn-danger" role="button" onclick="mostrarModal('${objetoindividual.id}')"> Eliminar </a>
                                 
                                </td>                               
            </tr>
       `;
    }
   
}
function mostrarModal(id){
    eliminandodato(id);

    myModalEliminar.show();
}

function eliminandodato(id){
     

    var datosEnviar={ 
        "id":id 
    }

    apiurl = apibase + apieliminar ;
    fetch(apiurl, 
        { 
            method: 'POST',
            body: JSON.stringify(datosEnviar)
        })
    .then(estructura => estructura.json())
    .then((datosrespuesta) => {
            completeDelete()
        })
    .catch(console.log);
}

function completeDelete(){
    tablaresultado.innerHTML = ``;
    consultardatos();
    myModalEliminar.hide();
}

consultardatos();
// //no necesariamente porque paso el objeto significa que el objeto se está pasando en objeto
// //hay dos maneras convertirlo en un string, en react ayuda. hay que hacerlo a pie
// //const es lo que estabamos usand para declarar estructuras estan la parte de const y let
//
function mostrarEditarModal(id, nombre, descripcion, tiempo){
    document.getElementById('id').value = id;
    document.getElementById('nombre').value = nombre;
    document.getElementById('descripcion').value = descripcion;
    document.getElementById('tiempo').value = tiempo;
    console.log(id, nombre, descripcion, tiempo);



    myModalEditar.show();
}


// formulario.addEventListener('submit', function(e)
// {
//     e.preventDefault();

//     var datosEnviar = {
//         "id":document.getElementById('id').value ,
//         "nombre":document.getElementById('nombre').value ,
//         "descripcion":document.getElementById('descripcion').value ,
//         "tiempo":document.getElementById('tiempo').value ,
//         "usuario":"Camilo" 
//     }
//     console.log(datoseditar);
    
//     apiurl = apibase + apieditar ;
//     fetch(apiurl, 
//         { 
//             method: 'POST',
//             body: JSON.stringify(datosEnviar)
//         })
//     .then(estructura => estructura.json())
//     .then((datosrespuesta) => {
//             completeEdit()
//         })
//     .catch(console.log);
// });

// function completeEdit(){
//     myModalEditar.hide();
//     tablaresultado.innerHTML = ``;
//     consultardatos();
//     //window.location = 'listarcurso.html';
// }

// consultardatos();


// //crear una funcion parecida a la de submit
// //cambiar el metodo insertar por el de editar
// //crear una funcion similar a completeDelete