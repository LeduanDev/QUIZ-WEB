document.addEventListener('DOMContentLoaded', function () {
    new Glider(document.querySelector('.glider'), {
      slidesToShow: 1,
      slidesToScroll: 1,
      draggable: true,
      dots: '.glider-dots',
      arrows: {
        prev: '.glider-prev',
        next: '.glider-next'
      },
      responsive: [
        {
          breakpoint: 768, // Pantallas pequeñas (tabletas en modo vertical)
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
          }
        },
        {
          breakpoint: 1024, // Pantallas medianas (tabletas en modo horizontal y portátiles)
          settings: {
            slidesToShow: 3,
            slidesToScroll: 2,
          }
        },
        {
          breakpoint: 1280, // Pantallas grandes (escritorios)
          settings: {
            slidesToShow: 4,
            slidesToScroll: 3,
          }
        }
      ]
    });
  });   