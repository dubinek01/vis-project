# Generated by Django 2.1.7 on 2020-01-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmallCinemaApp', '0004_reservation_seat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='phonenumber',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surename',
        ),
        migrations.AddField(
            model_name='childrenticket',
            name='seat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeType',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='EmployeeType',
        ),
    ]