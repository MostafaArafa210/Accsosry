from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customer"
    )
    name=models.CharField(max_length=90,null=False)
    email=models.EmailField(max_length=90,null=False)
    age=models.CharField(max_length=60,null=True,blank=True)
    create_dt=models.DateTimeField(auto_now_add=True)
    imge=models.ImageField(null=True,blank=True,upload_to='media/image/',default='media/image/Pic.png')
    phone=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name=models.CharField(max_length=90,null=False)


    def __str__(self):

        return self.name


class Necklace(models.Model):
    CATEGORY = (
        ('pendant', 'pendant'),
        ('princess', 'princess'),
        ('choker', 'choker'),
        ('collar', 'collar'),
        ('opera', 'opera'),
        ('charm', 'charm'),
        ('matinée', 'matinée'),
        ('multi-chain', 'multi-chain'),
        ('locket', 'locket'),
    )
    name=models.CharField(max_length=90,null=False)
    price=models.FloatField()
    category=models.CharField(max_length=300,null=False,choices=CATEGORY)
    tag=models.ManyToManyField(Tag)
    data_create=models.DateTimeField(auto_now_add=True,null=True)
    descripion=models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS=(
        ('in_progress','in_progress'),
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('out_stock', 'out_stock'),
        ('out_of_order', 'out_of_order')
    )
    data_create=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=150,choices=STATUS,null=True)
    customers=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    tag=models.ManyToManyField(Tag)
    iteam=models.ForeignKey(Necklace,on_delete=models.CASCADE,null=True)

