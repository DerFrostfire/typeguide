from django.db import models
from django.dispatch import receiver
import random

class Module(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    lessons = models.ManyToManyField("Lesson", blank=True)

class Lesson(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content_html = models.TextField()