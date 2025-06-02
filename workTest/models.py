from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User

CONDITION_CHOICES = [
    ('new', 'Новое'),
    ('perfect', 'Отличное'),
    ('good', 'Хорошее'),
    ('satisfactory', 'Удовлетворительное'),
    ('broken', 'Требует ремонта'),
]

CATEGORY_CHOICES = [
    ('book', 'Книги'),
    ('table', 'Столы'),
    ('clother', 'Одежда'),
    ('toys', 'Игрушки')
]

STATUS_CHOICES = [
    ('pending', 'На рассмотрении'),
    ('accepted', 'Принято'),
    ('rejected', 'Отклонено'),
    ('completed', 'Завершено')
]


class Ad(models.Model):
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=20, default='')
    category = models.CharField(max_length=20, default='new', choices=CATEGORY_CHOICES, verbose_name='Категория товара')

    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='good',
                                 verbose_name='Состояние товара')
    created_at = models.DateTimeField(max_length=20, auto_now_add=True)
    is_active = models.BooleanField(default=True)

class ExchangeProposal(models.Model):
    ad_sender = models.ForeignKey(Ad, max_length=20, default='', on_delete=models.SET_NULL, null=True,
                                  related_name='sender')
    ad_receiver = models.ForeignKey(Ad, max_length=20, default='', on_delete=models.SET_NULL, null=True,
                                    related_name='receiver')
    comments = models.CharField(max_length=20, default='')
    offered_item = models.ForeignKey(Ad, default='', related_name='offered_item', on_delete=models.CASCADE)
    desired_item = models.ForeignKey(Ad, default='', related_name='desired_item', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending', choices=STATUS_CHOICES)
    created_at = models.DateTimeField(max_length=20, auto_now_add=True)

