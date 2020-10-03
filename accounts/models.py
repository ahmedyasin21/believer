from django.urls import reverse
from django.db import models
from django.contrib import auth
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    # email = models.EmailField(("Email Address"), max_length=254)
    def __str__(self):
        return "@{}".format(self.username)

class UserProfile(models.Model):

    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    # author = models.ForeignKey(Post, on_delete=models.CASCADE)
    avatar = models.ImageField(("Avatar"), upload_to='displays', default = 'default.png',height_field=None, width_field=None, max_length=None,blank = True)
    slug = models.SlugField(blank = True)
    create_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.user.username} UserProfile'
    
    def save(self,*args, **kwargs):
        super(UserProfile,self).save(*args, **kwargs) #it will take data and save it

        dp = Image.open(self.avatar.path) #storing avatar in varible
        if dp.height >300 or dp.width >300:
            output_size =(300,300) #set anysize you want
            dp.thumbnail(output_size) 
            dp.save(self.avatar.path) #after resing it save it in data base in place of uploaded once by user

    def get_absolute_url(self):
        return reverse("userprofile_detail", kwargs={"pk": self.pk})

@receiver(post_save,sender=auth.models.User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save,sender=auth.models.User)
def save_profile(sender,instance,**kwargs):
    instance.userprofile.save()

class Contact(models.Model):

    from_user = models.EmailField(max_length=254)
    subject = models.CharField( max_length=150)
    message = models.TextField()
    to_user = models.EmailField( max_length=254)
    create_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.from_user

    def get_absolute_url(self):
        return reverse("accounts:sent_confirm", kwargs={"pk": self.pk})


# class Profile(models.Model):
#     user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
#     email_confirmed = models.BooleanField(default=False)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# class Code(models.Model):

#     def __str__(self):
#         return self.vcode

  