var cantidadDeClases = 3;
var clases = {};


document.addEventListener("DOMContentLoaded", function(event) { 
    for (let i = 0; i<cantidadDeClases; i++){
        let idDeContenido = "contenido-" + parseInt(i+1);
        let idDeTareas = "tareas-" + parseInt(i+1);
        let idDeConceptos = "conceptos-" + parseInt(i+1);
        let idDeCarrusel = "carrusel-" + parseInt(i+1);
        let idDeCodigo = "codigo-" + parseInt(i+1);

        let contenido = document.getElementById(idDeContenido);
        let tareas = document.getElementById(idDeTareas);
        let conceptos = document.getElementById(idDeConceptos);
        let carrusel = document.getElementById(idDeCarrusel);
        let codigo = document.getElementById(idDeCodigo);

        clases[i]= {};

        clases[i]["contenido"] = contenido;
        clases[i]["carrusel"] = carrusel;
        clases[i]["tareas"] = tareas;
        clases[i]["conceptos"] = conceptos;
        clases[i]["codigo"] = codigo;
    }
});

var mostrarContenidoClase = function(nroClase, tipoContenido){
    if(tipoContenido){
        for (let i = 0; i<cantidadDeClases; i++){
            if(i != nroClase && clases[i] && clases[i]["contenido"]){
                clases[i]["contenido"].style.display = 'none';
            } else if(clases[i]["contenido"]){
                for (const [key, value] of Object.entries(clases[i])) {
                    clases[i]["contenido"].style.display = 'block'
                    if(key == tipoContenido){
                        clases[i][tipoContenido].style.display = 'block';
                    } else if (key !== 'carrusel' && key !== 'contenido'){
                        clases[i][key].style.display = 'none';
                    }
                }
            }
        }
    } else {
        for (let i = 0; i<cantidadDeClases; i++){
            if(i != nroClase){
                clases[i]["carrusel"].style.display = 'none';
            } else {
                clases[i]["carrusel"].style.display = 'block';
            }
        }
        
    }
    
}
