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
"""

