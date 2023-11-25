var formulario = document.getElementById('formulario');
const modalSuccess = new bootstrap.Modal(document.getElementById('modalSuccess'));
const modalUnsuccess = new bootstrap.Modal(document.getElementById('modalUnsuccess')); 
var apibase = "https://paginas-web-cr.com/ApiPHP/apis/";
var apiauthenticate = "AutenticarUsuario.php"; 
var apicorreo = "SendPassword.php";

formulario.addEventListener('submit', function(e) {
    e.preventDefault();
    
    var email = document.getElementById('usuario').value;
    var password = document.getElementById('contraseña').value;

    var credentials = {
        email: email,
        password: password,
    };

    authenticateUser(credentials);
});

function authenticateUser(credentials) {
    apiurl = apibase + apiauthenticate;
    fetch(apiurl, {
            method: 'POST',
            body: JSON.stringify(credentials)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                modalSuccess.show();
                completeAuthentication();
            } else {
                modalUnsuccess.show();
            }
        })
        .catch(console.log);
}

function completeAuthentication() {
    window.location = 'PaginaPrincipal.html';
}


modalUnsuccess.addEventListener('submit', function(e)
{
    e.preventDefault();
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
    .catch(console.log);
});

function completeInsert(){
    window.location = 'indexiniciarsesion.html';
}

