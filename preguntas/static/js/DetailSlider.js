document.addEventListener('DOMContentLoaded', function(){
    var glider = new Glider(document.querySelector('.glider'), {
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        dots: '.dots',
        rewind: true, // Hace que vuelva al principio cuando termina
        duration: 0.5
    });

    // Función para mover el slider automáticamente
    function autoPlayGlider() {
        setInterval(function(){
            glider.scrollItem('next');
        }, 3000); // Cambia cada 3 segundos
    }

    // Llamamos a la función para empezar la reproducción automática
    autoPlayGlider();
});