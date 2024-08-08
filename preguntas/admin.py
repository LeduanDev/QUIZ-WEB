
from django.contrib import admin
from .models import Question, Choice, Category,Section



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Section)