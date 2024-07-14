# Generated by Django 5.0.7 on 2024-07-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_anna', '0006_alter_pdfmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='otziv/', verbose_name='Фото отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]