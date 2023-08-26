var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apiconsultar = "ListaEstudiantes.php";
var apieliminar = "BorrarEstudiantes.php";
var apieditar = "ActualizarEstudiantes.php";

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
                                <td>${objetoindividual.cedula}</td>
                                <td>${objetoindividual.correoelectronico}</td>
                                <td>${objetoindividual.telefono}</td>
                                <td>${objetoindividual.telefonocelular}</td>
                                <td>${objetoindividual.fechanacimiento}</td>
                                <td>${objetoindividual.sexo}</td>
                                <td>${objetoindividual.nombre}</td>
                                <td>${objetoindividual.apellidopaterno}</td>
                                <td>${objetoindividual.apellidomaterno}</td>
                                <td>${objetoindividual.nacionalidad}</td>
                                <td>${objetoindividual.idCarreras}</td>
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

consultardatos();