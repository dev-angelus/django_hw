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


class CarReview(models.Model):
    RATINGS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )

    car_review = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comment_object", null=True)
    text = models.TextField(null=True)
    rate_stars = models.CharField(max_length=100, choices=RATINGS, default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)


def __str__(self):
    return self.rate_stars


class User(models.Model):

    name = models.CharField("Ваше имя:", max_length=100)
    lastname = models.CharField("Ваша фамилия:", max_length=100)
    email = models.CharField("Ваш e-mail:", max_length=100)
    feedback_text = models.TextField("Ваш отзыв:", max_length=200)

    def __str__(self):
        return self.feedback_text

