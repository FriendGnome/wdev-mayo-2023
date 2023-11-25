menuprincipal.innerHTML += `
<nav class="navbar navbar-expand-lg bg-body-tertiary btn btn-danger">
                    <div class="container-fluid">
                    <a class="navbar-brand text-white" href="IndexPaginaPrincipal.html">Página Principal</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <a class="navbar-brand text-white" href="https://paginas-web-cr.com/ApiPHP">API</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Opciones de Crear
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="crearcurso.html">Crear Cursos</a></li>
                                <li><a class="dropdown-item" href="crearestudiante.html">Crear Estudiantes</a></li>
                                <li><a class="dropdown-item" href="creargrupo.html">Crear Grupos</a></li>
                                <li><a class="dropdown-item" href="crearprofesor.html">Crear Profesores</a></li>
                            </ul>
                        </li>
                        </ul>        
                        </form>
                    </div>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Opciones de Listar
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="listarcurso.html">Listar Cursos</a></li>
                                <li><a class="dropdown-item" href="listarestudiante.html">Listar Estudiantes</a></li>
                                <li><a class="dropdown-item" href="listargrupo.html">Listar Grupos</a></li>
                                <li><a class="dropdown-item" href="listarprofesor.html">Listar Profesores</a></li>
                            </ul>
                        </li>
                        </ul>        
                        </form>
                    </div>
                    </div>
                </nav>`;

footer.innerHTML += `
<footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
          <p class="col-md-4 mb-0 text-muted">© 2023 Website de Camilo</p>
          <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
            <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
          </a>      
          <ul class="nav col-md-4 justify-content-end">
            <li class="nav-item"><a href="IndexPaginaPrincipal.html" class="nav-link px-2 text-muted">Página Principal</a></li>
          </ul>
        </footer>`;