from django.db import models
from django.urls import reverse
from django.utils import timezone


class VideosList(models.Model):

    list_title = models.CharField(max_length=255)
    list_cover = models.ImageField(upload_to='list cover', height_field=None, width_field=None, max_length=None,blank =True)
    create_date = models.DateField(default = timezone.now)
    discription= models.TextField(("List discription"),blank=True)

    def __str__(self):
        return self.list_title

class VideosModel(models.Model):

    
    videos_lists = models.ForeignKey(VideosList,on_delete=models.CASCADE) 
    video_title = models.CharField(max_length=250)
    video_url = models.URLField(max_length=1200)
    video_discription = models.TextField()
    create_date = models.DateField(default = timezone.now)


    def __str__(self):
        return self.video_title

    # def get_absolute_url(self):
    #     return reverse("videos_detail", kwargs={"pk": self.pk})


# Create your models here.
