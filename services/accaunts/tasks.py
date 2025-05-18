from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()  # Здесь мы связаваем get_user_model() с user чтобы была возможность делать к User запросы get и filter

@shared_task
def user_del_not_verefications(user_id):
    from allauth.account.models import EmailAddress
    try:  # Проверка на ошибка если пользователь удалил сам запись раньше времени
        user = User.objects.get(id = user_id)
        email_now = EmailAddress.objects.get(user = user)  # Почему мы здесь изпользуем get а не filter? Потомучто get ищет один обьект а filter масив
                                                           # У нас же на один акк может быть только одна почта поэтому get более оптимизированно
        if not email_now.verified:
            email_now.delete()
            user.delete()
    except (User.DoesNotExist, EmailAddress.DoesNotExist):  # Почему именно такя ошибка? Потомучто оригинальная ошибка которая вылезет именно здесь
                                                            # Еще может быть ошибка что найдено больше одной записи но это у нас невозможно ибо в настройках прописано 1 аккаунь на 1 почту
        pass