# Generated by Django 4.1.1 on 2022-10-02 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfsite', '0004_alter_credits_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.users'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='credit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.credits'),
        ),
    ]
