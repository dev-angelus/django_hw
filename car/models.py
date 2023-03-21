from django.db import models


class Car(models.Model):
    CAR_TYPE = (
        ('Седан','Седан'),
        ('Кросс-овер', 'Кросс-овер'),
        ('Внедорожник', 'Внедорожник'),
        ('Универсал','Универсал')
    )
    title = models.CharField("Название машины:", max_length=100)
    year = models.CharField("Год выпуска:", max_length=100)
    fuel_type = models.CharField("Топливо: ", max_length=100)
    engine_size = models.CharField("Объем двигателя: ", max_length=100)
    transmission = models.CharField("КП: ", max_length=100)
    body_type = models.CharField("Тип кузова: ", max_length=100, choices=CAR_TYPE)
    power = models.CharField("Мощность двигателя: ", max_length=100)
    seat = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    extra_parameters = models.TextField(null=True)
    image = models.ImageField(upload_to="")
    created_date = models.DateTimeField(auto_now_add=True)

    # video = models.URLField(max_length=100, null=True)
    # url = models.URLField(max_length=100)

    def __str__(self):
        return self.title

