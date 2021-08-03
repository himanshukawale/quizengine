from django.db import models
# from django.db.models.fields import BLANK_CHOICE_DASH

class User(models.Model):
    Name = models.TextField()
    Email = models.EmailField()
    time_history = models.TextField(null=True, blank=True)
    result = models.CharField(null=True, blank=True, max_length=25)
    def __str__(self):
        return self.Name

class Question(models.Model):
    Question_ID = models.TextField()
    Image_file = models.TextField(blank = True, null=True)
    Question_type = models.TextField()
    Question_text = models.TextField()
    Option_A = models.TextField(blank=True, null=True)
    Option_B = models.TextField(blank=True, null=True)
    Option_C = models.TextField(blank=True, null=True)
    Option_D = models.TextField(blank=True, null=True)
    Answer = models.TextField()
    def __str__(self):
        return self.Question_ID