# Generated by Django 3.0.2 on 2020-04-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_remove_answer_hw_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_no',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]