from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    decription = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name