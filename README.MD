# Save for using Django's model

## Import
```
from polls.models import Question, Choice
from django.utils import timezone
```

## Question
### To create an object Question and save it:
```
q = Question(question_text="What's new", pub_date=timezone.now())
q.save()
```

### Select & filter
```
Question.objects.all()
Question.objects.get(pk=1)
Question.objects.filter(question_text__startswith='What')
Question.objects.get(id=1)
```

### Create choices for a question
```
q = Question.objects.get(pk=1)
q.choice_set.all() # All choice sets
q.choice_set.create(choice_text='Hello', votes=0)
```

### Inline
- TabularInline
- StackedInline

### https://docs.djangoproject.com/en/1.7/ref/templates/api/#template-loaders