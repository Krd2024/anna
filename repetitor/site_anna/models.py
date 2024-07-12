from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=12)


class Review(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(
        verbose_name="Оценка",
        choices=[
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return self.text
