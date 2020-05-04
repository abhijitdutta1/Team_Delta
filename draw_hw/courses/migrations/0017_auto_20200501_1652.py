# Generated by Django 3.0.2 on 2020-05-01 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0016_auto_20200425_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerinstructor',
            name='question_no',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answerstudent',
            name='question_no',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='answerinstructor',
            unique_together={('question_no', 'assignment')},
        ),
        migrations.AlterUniqueTogether(
            name='answerstudent',
            unique_together={('question_no', 'assignment', 'student')},
        ),
    ]