from django.db import models
# from cartapp.models import Orders

# # Create your models here.
class PayerDetails(models.Model):
    # order = models.Foreignkey(Orders, on_delete=models.CASACADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    city = models.CharField(max_length=100, null=True)

    def get_full_name(self):
        return self.firstname + self.lastname
 
    def __str__(self):
        return self.firstname
