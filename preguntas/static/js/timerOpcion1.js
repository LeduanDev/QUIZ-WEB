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
          alert("El tiempo se ha agotado, el quiz finalizará automáticamente.");
      
          // Imprimir las respuestas seleccionadas para depurar
      
          timeLeftInput.value = timeLeft;  // Actualiza el valor del campo oculto
      
          setTimeout(function() {
              form.submit();  // Envía el formulario automáticamente después de un breve retraso
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
  

  def quiz_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    questions = Question.objects.filter(category=category)
    seccion_id = category.section.id
    id_quizz = category.id
    enable_timer = category.enable_timer  # Verificamos si el temporizador está habilitado
    quiz_duration = category.quiz_duration

    total_score = 0
    correct_answers = 0
    unanswered_questions = 0

    if request.method == 'POST':
        # Verificar el tiempo restante enviado desde el frontend
        time_left = int(request.POST.get('time_left', 0))

        # Si el tiempo se ha agotado, se calcularán los resultados con las respuestas enviadas hasta el momento
        if enable_timer and time_left <= 0:
            # Aquí podemos manejar el caso donde el tiempo ha expirado
            print("El tiempo se ha agotado. Procesando las respuestas enviadas.")

        # Procesar el quiz normalmente (incluso si el tiempo se agotó)
        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))

            if selected_choice_id:
                selected_choice = question.choice_set.filter(pk=selected_choice_id).first()
                if selected_choice and selected_choice.is_correct:
                    total_score += question.points
                    correct_answers += 1
            else:
                unanswered_questions += 1

        total_questions = len(questions)
        incorrect_answers = total_questions - correct_answers
        percentage_correct = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        percentage_correct = round(percentage_correct, 1)
        total_score = min(total_score, 100)

        # Redirigir directamente a la página de resultados sin necesidad de una página de "tiempo agotado"
        return render(request, 'paginas/result.html', {
            'total_score': total_score,
            'correct_answers': correct_answers,
            'total_questions': total_questions,
            'unanswered_questions': unanswered_questions,
            'incorrect_answers': incorrect_answers,
            'percentage_correct': percentage_correct,
            'seccion_id': seccion_id,
            'id_quizz': id_quizz,
        })

    return render(request, 'paginas/quiz.html', {
        'questions': questions,
        'category': category,
        'enable_timer': enable_timer,  # Solo si el temporizador está habilitado
        'quiz_duration': quiz_duration  # Pasamos el tiempo estipulado
    })

