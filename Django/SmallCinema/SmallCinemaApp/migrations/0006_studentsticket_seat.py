# Generated by Django 2.1.7 on 2020-01-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmallCinemaApp', '0005_auto_20200116_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsticket',
            name='seat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
