from django.db import models
from django.contrib.auth import get_user_model
from fashionapp.models import Product
from paymentsapp.models import PayerDetails

# Create your models here.

# Get the user model
User = get_user_model()


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

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
   
    def __str__(self):
        return f'{self.user.username}  GHS{self.total}'
        

class Orders(models.Model):
    ordered_by = models.ForeignKey(PayerDetails, on_delete=models.CASCADE)
    items = models.TextField()
    total = models.FloatField()
    delivered = models.BooleanField(default=False)
    amount_paid = models.FloatField(default=1)
    transaction_id = models.PositiveIntegerField(default=2)
    tx_ref = models.CharField(max_length=50, null=True)
    note = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.ordered_by}  GHS {self.total}'
