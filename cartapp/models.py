from django.db import models
from django.contrib.auth import get_user_model
from fashionapp.models import Product

# Create your models here.

# Get the user model
User = get_user_model()


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.name} of '

    # def __str__(self):
    #     return str(self.item)


# Order Model
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
 
    def __str__(self):
        return f'{self.user.username}  ${self.total}'
        

class Orders(models.Model):
    items = models.TextField()
    user = models.CharField(max_length=255)
    total = models.FloatField()
    delivered = models.BooleanField(default=False)
