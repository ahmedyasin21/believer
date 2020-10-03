from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Questions(models.Model):
    CAT_CHOICES = (
    ('one','Week one'),
    ('two','Week two'),
    ('three','Week three'),
    ('four','Week four')
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

# class Week(models.Model):

#     weekend = models.CharField(("Week"), max_length=50)
#     create_date = models.DateField(default = timezone.now)

#     def __str__(self):
#         return self.weekend

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})



# class Quiz(models.Model):

#     # quiz = models.CharField(max_length=50,blank=True,default= 'quiz')
#     week = models.ForeignKey(Week, on_delete=models.CASCADE)
#     question_text = models.CharField(("Question"), max_length=1000)
#     answer = models.CharField(max_length=50)
#     create_date = models.DateField(default = timezone.now)
#     options1 = models.CharField(("option-1"), max_length=150)
#     options2 = models.CharField(("option-2"), max_length=150)
#     options3 = models.CharField(("option-3"), max_length=150)
#     options4 = models.CharField(("option-4"), max_length=150)

#     def __str__(self):
#         return self.question_text

#     def get_absolute_url(self):
#         return reverse("quiz_detail", kwargs={"pk": self.pk})

# # class Solution(models.Model):

   
# #     question = models.ForeignKey(Quiz, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.answer

# #     def get_absolute_url(self):
# #         return reverse("_detail", kwargs={"pk": self.pk})
