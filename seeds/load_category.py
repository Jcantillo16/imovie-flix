import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.movies.models import Category


def load_category():
    categories = [
        "Terror",
        "Suspenso",
        "Drama",
        'Comedia',
        'Accion',
    ]

    for category in categories:
        if not Category.objects.filter(name=category).exists():
            Category.objects.create(name=category)

    print("Categories loaded successfully")


load_category()
