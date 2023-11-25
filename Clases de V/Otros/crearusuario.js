var formulario = document.getElementById('formulario')
const modalSuccess = new bootstrap.Modal(document.getElementById('modalSuccess'))
var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apicrear = "InsertarUsuarios.php";
var apicorreo = "SendPassword.php";

formulario.addEventListener('submit', function(e)
{
    e.preventDefault();
    modalSuccess.show();
    var datosEnviar = {
        "name":document.getElementById('name').value ,
        "password":document.getElementById('password').value ,
        "email":document.getElementById('email').value ,
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

function enviarpassword(){
    var datosEnviar = {
        "email":document.getElementById('usuariocorreo').value ,
    }
        apiurl = apibase + apicorreo;
        fetch(apiurl, {
                method: 'POST',
                body: JSON.stringify(datosEnviar)
            })
            .then(estructura => estructura.json())
            .then((datosrespuesta) => {
            modalSuccess.show()
            completeInsert()
        })
}


function completeInsert(){
    enviarpassword()
    window.location = 'indexiniciarsesion.html';
}

