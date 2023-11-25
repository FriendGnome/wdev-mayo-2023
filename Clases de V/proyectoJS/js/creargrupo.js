var formulario = document.getElementById('formulario')
const modalSuccess = new bootstrap.Modal(document.getElementById('modalSuccess'))
var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apicrear = "InsertarGrupo.php";

formulario.addEventListener('submit', function(e)
{
    e.preventDefault();
    modalSuccess.show();
    var datosEnviar = {
        "nombre":document.getElementById('nombre').value ,
    }

    apiurl = apibase + apicrear ;
    fetch(apiurl, 
        { 
            method: 'POST',
            body: JSON.stringify(datosEnviar)
        })
    .then(estructura => estructura.json())
    .then((datosrespuesta) => {
            modalSuccess.show()
            completeInsert()
        })
    .catch(console.log);
});

function completeInsert(){
    window.location = 'listargrupo.html';
}