from .models import User, ConfirmEmailToken
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from orders_shop.celery import app as celery_app


@celery_app.task
def new_user_registered_signal_tasks(instance: User):
    """
     отправляем письмо с подтрердждением почты

"""

    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=instance.pk)

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {instance.email}",

        # message:
        token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [instance.email]
    )
    msg.send()


def new_order_signal_tasks(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
