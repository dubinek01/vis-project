# Generated by Django 2.1.7 on 2020-01-23 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmallCinemaApp', '0007_auto_20200122_1503'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adultsticket',
            unique_together={('showtime', 'seat')},
        ),
        migrations.AlterUniqueTogether(
            name='childrenticket',
            unique_together={('showtime', 'seat')},
        ),
        migrations.AlterUniqueTogether(
            name='studentsticket',
            unique_together={('showtime', 'seat')},
        ),
    ]