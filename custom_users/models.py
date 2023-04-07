from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    ADMIN = 1
    VIPClient = 2
    CLIENT = 3

    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (VIPClient, "VIPClient"),
        (CLIENT, "Client")
    )

    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_TYPE = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER")
    )

    MARRIED = 1
    SINGLE = 2
    COMPLICATED = 3

    MARITAL_STATUS = (
        (MARRIED, 'MARRIED'),
        (SINGLE, 'SINGLE'),
        (COMPLICATED, 'COMPLICATED')
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField('Номер телефона', max_length=100)
    age = models.PositiveIntegerField('Ваш возраст')
    user_type = models.IntegerField('Тип пользователя', choices=USER_TYPE)
    gender = models.IntegerField('Пол', choices=GENDER_TYPE)
    citizenship = models.CharField('Гражданство', max_length=100)
    city = models.CharField('Город', max_length=100)
    marital_status = models.IntegerField('Семейное положение', choices=MARITAL_STATUS)