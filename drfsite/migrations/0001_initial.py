# Generated by Django 4.1.1 on 2022-10-01 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('issuance_date', models.DateField()),
                ('return_date', models.DateField()),
                ('actual_return_date', models.DateField()),
                ('body', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('login', models.CharField(max_length=20)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('period', models.DateField()),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.dictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('credit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.credits')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.dictionary')),
            ],
        ),
        migrations.AddField(
            model_name='credits',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfsite.users'),
        ),
    ]
