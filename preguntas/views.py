import math
from django.shortcuts import render, get_object_or_404
from .models import Category, Question, Choice, Section
from django.db.models import Count

def home_view(request):
    categories = Category.objects.all()
    section = Section.objects.all()
    return render(request, 'paginas/home.html', {'categories': categories, 'section': section})


## Vista donde se mostraran las categorias por sección
def categoriasSeccion(request, seccion_id=None):
    seccion = get_object_or_404(Section, pk=seccion_id)
    categorias = Category.objects.filter(section=seccion)
    
    return render(request, 'paginas/Vcategorias.html', {
        'seccion': seccion,
        'categorias': categorias
    })


## Vista que contendrá todas las secciones disponibles
def allSection(request):
    filter_query = request.GET.get('filter', '')
    section = Section.objects.filter(nombre__icontains=filter_query)
    return render(request, 'paginas/Vsection.html', {'section': section, 'filter_query': filter_query})


def details(request, categorie_id):
    categorie =  get_object_or_404(Category, pk=categorie_id)
    question_count = categorie.question_set.count()
    return render(request, 'paginas/quizzDetails.html', {
        'categorie': categorie,
        'question_count': question_count
    })



def quiz_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    questions = Question.objects.filter(category=category)
    seccion_id = category.section.id 
    id_quizz = category.id 

    total_score = 0
    correct_answers = 0
    unanswered_questions = 0

    if request.method == 'POST':
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

        # Calcular el porcentaje de respuestas correctas
        rounder = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        
        percentage_correct = round(rounder,1)

        # Asegurarse de que el puntaje total no exceda 100
        total_score = min(total_score, 100)

        # Calcular stroke-dasharray y stroke-dashoffset
        radius = 40
        stroke_dasharray = 2 * math.pi * radius
        stroke_dashoffset = stroke_dasharray * (1 - percentage_correct / 100)

        return render(request, 'paginas/result.html', {
            'total_score': total_score,
            'correct_answers': correct_answers,
            'total_questions': total_questions,
            'unanswered_questions': unanswered_questions,
            'incorrect_answers': incorrect_answers,
            'percentage_correct': percentage_correct,
            'stroke_dasharray': stroke_dasharray,
            'stroke_dashoffset': stroke_dashoffset,
            'seccion_id': seccion_id,
            'id_quizz' : id_quizz,
        })

    return render(request, 'paginas/quiz.html', {'questions': questions, 'category': category})




