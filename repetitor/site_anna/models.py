from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator


class User(AbstractUser):

    email_validator = EmailValidator()
    phone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(
        _("email address"),
        unique=False,
        blank=False,
        null=False,
        validators=[email_validator],
    )
    on_the_list = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     self.email = self.normalize_email(self.email)
    #     super().save(*args, **kwargs)


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
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, verbose_name="Ползователь", unique=False
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return self.text


class PdfModel(models.Model):
    name = models.TextField(max_length=20)
    pdf_file = models.FileField(
        upload_to="pdf_files/", blank=True, null=True, verbose_name="PDF документы"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время загрузки файла "
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы "

    def __str__(self):
        return str(self.pdf_file)


class Achievement(models.Model):
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Достижение"

    # def __str__(self):
    #     return self.text[:50] + "..."


class PhotoReview(models.Model):
    image = models.ImageField(upload_to="photo/", verbose_name="Фото ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.image.url


from django.db import models


class StudentAchievement(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя ученика")
    text = models.TextField(verbose_name="Текст достижения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Достижение ученика"
        verbose_name_plural = "Достижения учеников"
