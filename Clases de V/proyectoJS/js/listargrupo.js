var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apiconsultar = "ListaGrupo.php";
var apieliminar = "BorrarGrupo.php";
var apieditar = "ActualizarGrupo.php";


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
                                <td>
                                <a name="Editar" id="Editar" class="btn btn-success" role="button" onclick="mostrarEditarModal('${objetoindividual.id}','${objetoindividual.nombre}')"> Editar </a> 
                                ||
                                <a name="Eliminar" id="Eliminar" class="btn btn-danger" role="button" onclick="mostrarModal('${objetoindividual.id}')"> Eliminar </a>
                                </td>                               
            </tr>
       `;
    }
   
}

consultardatos();

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

function mostrarEditarModal(id, nombre){
    document.getElementById('id').value = id;
    document.getElementById('nombre').value = nombre;
    console.log(id, nombre);

    myModalEditar.show();
}

consultardatos();

formulario.addEventListener('submit', function(e)
{
    e.preventDefault();

    var datosEnviar = {
        "id":document.getElementById('id').value ,
        "nombre":document.getElementById('nombre').value 
    }
    
    apiurl = apibase + apieditar ;
    fetch(apiurl, 
        { 
            method: 'POST',
            body: JSON.stringify(datosEnviar)
        })
    .then(estructura => estructura.json())
    .then((datosrespuesta) => {
            completeEdit()
        })
    .catch(console.log);
});

function completeEdit(){
    myModalEditar.hide();
    tablaresultado.innerHTML = ``;
    consultardatos();
    //window.location = 'listarcurso.html';
}