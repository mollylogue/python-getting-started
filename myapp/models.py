from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

class Folder(models.Model):
    name = models.CharField(max_length=30)
    topic = models.ManyToManyField(Topic, blank=True, related_name='folders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='documents')
    topic = models.ManyToManyField(Topic, blank=True, related_name='documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
