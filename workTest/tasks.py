from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_exchange_notification(user_email, item_name):
    print("✅ Задача запущена!")  # Проверка получения задачи
    try:
        subject = f"Новое предложение по вашему товару {item_name}"
        message = "Кто-то предложил обмен!"
        send_mail(
            subject, message, "web_16px@mail.ru", [user_email], fail_silently=False
        )
        return "Письмо отправлено!"
    except Exception as e:
        print(e)
        return None
