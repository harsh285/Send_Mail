from django.db import models

# Create your models here.
class TakeEmail(models.Model):
    recepient_email = models.EmailField(default='abc@gmail.com')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recepient_email


class Information(models.Model):
    product_name = models.CharField(max_length=256, null=False, unique=True)
    Category = models.CharField(max_length=256)
    Qty = models.CharField(max_length=256)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name