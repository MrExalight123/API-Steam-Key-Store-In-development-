from django.apps import AppConfig


class AccauntsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accaunts'
    
    def ready(self):
        from . import signals  # Задаеться вопрос значем мы тут это импортируем? 
                         # А импортируем мы это чтобы сигналы видели приложения и была гарантия что она увидит тот диапазон памяти который мы хотим чтобы она увидела
                         # Ключевая функция тут лежит не в самом apps.py а в самом ready
                         # ибо после того как django увидел этот обьект в setting.py django ищет все ready и запускает ровно по одному разу у каждого AppConfig
                         # Почему мы не пишим это в views 
                         # Потомучто в views нету гарантии что все сработает как надо ибо пользователь может создаться через API
                         # к примеру или вообще views не видить ту область памяти
                         # Так же надо прописовать этот класс в setting для правильной работы
