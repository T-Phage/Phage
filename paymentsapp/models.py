from django.db import models
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# Create your models here.

class PayerDetails(models.Model):
    # order = models.Foreignkey(Orders, on_delete=models.CASACADE)
    payer = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    othername = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    

    def get_full_name(self):
        # The user is identified by their email address
        return self.payer 

    # class Meta:
    #     verbose_name_plural = 'Users'

    def __str__(self):
        return self.payer.username
