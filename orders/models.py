from django.db import models


class Order(models.Model):
    number = models.IntegerField(null=False, unique=True)
    dollar_cost = models.FloatField(null=False)
    delivery_date = models.DateField(null=False)
    ruble_cost = models.FloatField(null=False)
