from django.db import models


class UserRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, default=True)
    password = models.CharField(max_length=20)
    create_date = models.CharField(null=True)


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    registered_user = models.ForeignKey(
        UserRegistration, on_delete=models.CASCADE, default="")


class UserToken(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    create_date = models.CharField(null=True)
    registered_user = models.ForeignKey(
        UserRegistration, on_delete=models.CASCADE, default="")
