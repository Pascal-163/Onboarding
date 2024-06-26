# Generated by Django 4.2.11 on 2024-05-10 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0003_choice_next_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['title'], 'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AddField(
            model_name='usersurvey',
            name='last_answer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.answer', verbose_name='Последний ответ'),
        ),
        migrations.AlterUniqueTogether(
            name='usersurvey',
            unique_together={('user', 'survey')},
        ),
    ]
