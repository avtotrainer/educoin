from django.db import models

# Create your models here.

# wallets/models.py
from django.db import models

class Wallet(models.Model):
    student_name = models.CharField(max_length=100, unique=True)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.student_name

