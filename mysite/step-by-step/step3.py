__author__ = 'PyBeaner'

# python manage.py shell
# you can manually setup django-shell environment
# export DJANGO_SETTINGS_MODULE=mysite.settings
import django
django.setup()

"""
from polls.models import Question,Choice
# nothing in the database yet
Question.objects.all()
[]

from django.utils import timezone
q = Question(question_text="What's new?",pub_date=timezone.now())
q.save()

q.id
# 1 or 1L

Question.objects.all()
[<Question: Question object>]


# Lookup API
Question.objects.filter(question_text__startswith='What')
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# use pk(PrimaryKey) instead of id,pk is always available
Question.objects.get(pk=1)

# create objects
q.choice_set.create(choice_text="The Sky",votes=1)

# deeper lookup
Choice.objects.filter(question__pub_date__startswith="What")
"""

