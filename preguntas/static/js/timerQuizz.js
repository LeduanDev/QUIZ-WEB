document.addEventListener("DOMContentLoaded", function() {
  var quizDataElement = document.getElementById('quiz-data');
  var timeLeft = parseInt(quizDataElement.getAttribute('data-duration'), 10);
  var timerElement = document.getElementById('timer');
  var form = document.querySelector('form');
  var timeLeftInput = document.getElementById('time-left');  // Campo oculto para el tiempo restante

  function updateTimer() {
      var minutes = Math.floor(timeLeft / 60);
      var seconds = timeLeft % 60;
      timerElement.textContent = `Tiempo restante: ${minutes}:${seconds < 10 ? '0' + seconds : seconds}`;

      timeLeftInput.value = timeLeft;  // Actualiza el valor del campo oculto

      if (timeLeft <= 0) {
          clearInterval(timerInterval);
          // Enviar el formulario automáticamente después de un breve retraso
          setTimeout(function() {
              form.submit();  
          }, 100); // Retraso de 100ms
      }

      timeLeft--;
  }

  var timerInterval = setInterval(updateTimer, 1000);
  updateTimer();  // Muestra el tiempo inicial

  form.addEventListener('submit', function() {
      clearInterval(timerInterval);  // Detener el temporizador al enviar el formulario
  });
});
