# Generated by Django 3.0.2 on 2020-04-24 03:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0014_registercourse'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registercourse',
            unique_together={('course', 'student')},
        ),
    ]
