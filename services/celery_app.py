import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.settings')

app = Celery('services')

# Загружаем настройки Celery из settings.py (все, что начинается с "CELERY_")
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автопоиск задач в установленных приложениях Django
app.autodiscover_tasks()
