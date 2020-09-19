from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


SIZE_CHOICE = [('XXS', 'XXS'),
               ('XS', 'XS-S'),
               ('S', 'S'),
               ('M', 'M'),
               ('M-L', 'L'),
               ('XL', 'XL'), ]

COLOR_CHOICE = [('Blacks', 'Blacks'),
                ('Whites', 'Whites'),
                ('Reds', 'Reds'),
                ('Greys', 'Greys'),
                ('Blues', 'Blues'),
                ('Beige Tones', 'Beige Tones'),
                ('Greens', 'Greens'),
                ('Yellows', 'Yellows'), ]


# Product Model
class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    size = models.CharField(max_length=5, choices=SIZE_CHOICE)
    color = models.CharField(max_length=15, choices=COLOR_CHOICE)
    label = models.CharField(max_length=40, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name

# class Outfit(models.Model):
#     type = models.CharField(max_length=25)
#     cat = models.CharField(max_length=255)
#
#
# SIZE_CHOICE = [('XXS', 'XXS'),
#                ('XS', 'XS-S'),
#                ('S', 'S'),
#                ('M', 'M'),
#                ('M-L', 'L'),
#                ('XL', 'XL'), ]
#
# CATEGORIES_CHOICE = [('men', 'men'),
#                      ('women', 'women'),
#                      ('kids', 'kids'),
#                      ('accessories', 'accessories'),
#                      ('cosmetics', 'cosmetics'), ]
#
# COLOR_CHOICE = [('Blacks', 'Blacks'),
#                 ('Whites', 'Whites'),
#                 ('Reds', 'Reds'),
#                 ('Greys', 'Greys'),
#                 ('Blues', 'Blues'),
#                 ('Beige Tones', 'Beige Tones'),
#                 ('Greens', 'Greens'),
#                 ('Yellows', 'Yellows'), ]
#
#
# class Products(models.Model):
#     name = models.CharField(max_length=100)
#     product_img = models.FileField(upload_to='media/products')
#     price = models.FloatField()
#     label = models.CharField(max_length=50, null=True)
#     outfit = models.ForeignKey(Outfit, null=True, on_delete=models.SET_NULL)
#     size = models.CharField(max_length=5, choices=SIZE_CHOICE)
#     category = models.CharField(max_length=20, choices=CATEGORIES_CHOICE)
#     stock = models.PositiveIntegerField()
#     color = models.CharField(max_length=15, choices=COLOR_CHOICE)
#
#
# class Cart(models.Model):
#     pass
