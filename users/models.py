from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name= models.CharField(max_length=20,default='')
    email =  models.EmailField(default ='')
    image = models.ImageField(default = 'default.jpg',upload_to='users')

    def __str__(self):
        return f'{self.user.username} ( {self.first_name} {self.last_name} )'

    # profile_picture = models
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
