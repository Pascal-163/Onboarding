# Generated by Django 4.2.11 on 2024-05-11 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_alter_usersurvey_last_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurvey',
            name='last_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='survey.choice', verbose_name='id последнего ответа'),
        ),
    ]
