from django.db import models
from django.urls import reverse

# Create your models here.

class Questions(models.Model):
    CAT_CHOICES = (
    ('week one','Week one'),
    ('week two','Week two'),
    ('week three','Week three'),
    ('week four','Week four')
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question