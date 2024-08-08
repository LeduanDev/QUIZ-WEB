
from django.shortcuts import render, get_object_or_404
from .models import Category, Question, Choice, Section



def home_view(request):
    categories = Category.objects.all()
    section = Section.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories, 'section': section})

def carousel(request):
    categories = Category.objects.all()
    section = Section.objects.all()
    return render(request, 'bloques/Bcategorias.html', {'categories': categories, 'section': section})



## Vista donde se mostraran las categorias por sección
def categoriasSeccion(request, seccion_id=None):
    seccion = get_object_or_404(Section, pk=seccion_id)
    categorias = Category.objects.filter(section=seccion)
    
    return render(request, 'quiz/Vcategorias.html', {
        'seccion': seccion,
        'categorias': categorias
    })

def quiz_view(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        questions = Question.objects.filter(category=category)
    else:
        questions = Question.objects.all()

    total_score = 0
    correct_answers = 0

    if request.method == 'POST':
        for question in questions:
            selected_choice = question.choice_set.get(pk=request.POST.get(str(question.id)))
            if selected_choice.is_correct:
                total_score += question.points
                correct_answers += 1

        return render(request, 'quiz/result.html', {
            'total_score': total_score,
            'correct_answers': correct_answers,
            'total_questions': len(questions)
        })

    return render(request, 'quiz/quiz.html', {'questions': questions, 'category': category})
