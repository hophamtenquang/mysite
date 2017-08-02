from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
	    ('Date published', {'fields': ['pub_date']}),
	    ('Title', {'fields': ['question_text']})
	]
	inlines = [ChoiceInline]
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
