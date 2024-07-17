# Generated by Django 5.0.7 on 2024-07-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_anna', '0003_pdfmodel_alter_review_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Достижение',
            },
        ),
        migrations.CreateModel(
            name='StudentAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя ученика')),
                ('text', models.TextField(verbose_name='Текст достижения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Достижение ученика',
                'verbose_name_plural': 'Достижения учеников',
            },
        ),
    ]