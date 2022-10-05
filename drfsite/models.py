from django.core.validators import FileExtensionValidator
from django.db import models


class Users(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    login = models.CharField(max_length=20)
    registration_date = models.DateField()


class Dictionary(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)


class Credits(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    issuance_date = models.DateField()
    return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    body = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.DecimalField(max_digits=10, decimal_places=2)


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    credit_id = models.ForeignKey(Credits, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE)


class Plans(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    period = models.DateField()
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
