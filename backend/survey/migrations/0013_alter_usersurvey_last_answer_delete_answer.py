# Generated by Django 4.2.11 on 2024-05-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_answer_alter_usersurvey_last_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurvey',
            name='last_answer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Последний ответ'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
