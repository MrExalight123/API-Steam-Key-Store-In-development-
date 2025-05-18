from .tasks import user_del_not_verefications
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def schedule_user_deletion(sender, request, user, **kwargs):
    user_del_not_verefications.apply_async((user.id,), countdown = 180)