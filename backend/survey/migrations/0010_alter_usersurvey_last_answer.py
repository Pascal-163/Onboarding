# Generated by Django 4.2.11 on 2024-05-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_alter_usersurvey_last_answer_delete_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurvey',
            name='last_answer',
            field=models.IntegerField(blank=True, null=True, verbose_name='Последний ответ'),
        ),
    ]
