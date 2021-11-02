from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    fb_id = models.PositiveBigIntegerField(unique=True, blank=False, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    score_value = models.PositiveIntegerField(blank=False, default=0)
    email = models.EmailField(blank=True, max_length=50, default='')


    def __str__(self):
        return self.fb_id
