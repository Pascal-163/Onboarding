# Generated by Django 4.2.11 on 2024-05-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0016_rename_response_usersurvey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersurvey',
            name='last_answer',
            field=models.IntegerField(blank=True, null=True, verbose_name='id последнего ответа'),
        ),
    ]