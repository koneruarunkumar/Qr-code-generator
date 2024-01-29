from django.db import models

class RegisterData(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=25)
    pwd=models.CharField(max_length=25)




class QRCodeData(models.Model):
    user_data = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
