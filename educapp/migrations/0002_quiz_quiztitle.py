# Generated by Django 5.0.4 on 2024-05-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quizTitle',
            field=models.TextField(default='quiz title no defined.'),
            preserve_default=False,
        ),
    ]
