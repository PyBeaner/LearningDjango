1. start new app
    
    django-admin startapp yourapp
    
2. add models

    define your model as a subclass of the django.db.models
        
3. make migrations
    
    python manage.py makemigrations [your_new_app]
    
4. do the migrations
    
    python manage.py migrate
    