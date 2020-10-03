from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Notes(models.Model):

    author = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    essay = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:notes_detail", kwargs={"pk": self.pk})
