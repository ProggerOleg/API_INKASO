# Generated by Django 4.1.1 on 2022-10-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='return_date',
            field=models.DateField(verbose_name='%dd/%m/%yy/'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]