from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from Necles.models import Customer



def customercreateprofile(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,

        )
        print('Crated Profile Succsesse')
post_save.connect(customercreateprofile,sender=User)