# Generated by Django 4.1.1 on 2022-10-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfsite', '0005_alter_credits_user_id_alter_payments_credit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='actual_return_date',
            field=models.DateField(verbose_name='d/m/y'),
        ),
    ]