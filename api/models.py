from django.db import models
import uuid

class Project(models.Model):
    name        = models.CharField(max_length=100)
    category    = models.CharField(max_length=100)
    description = models.TextField()
    link        = models.URLField(blank=True)
    code        = models.TextField()
    enterdata_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name         = models.CharField(max_length=100)
    is_client    = models.BooleanField(default=False)
    is_data_donor= models.BooleanField(default=False)
    email        = models.EmailField(max_length=150, unique=True)
    password     = models.CharField(max_length=128)
    university   = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    experience  = models.PositiveIntegerField(default=0)
    projects    = models.TextField(blank=True)
    about_me    = models.TextField(blank=True)
    languages   = models.CharField(max_length=200, blank=True)
    skillset    = models.TextField(blank=True)

    def __str__(self):
        return f'Profile of {self.user.email}'


class Subject(models.Model):
    name  = models.CharField(max_length=100)
    mark  = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link        = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Dataset(models.Model):
    name        = models.CharField(max_length=200)
    dtype       = models.CharField(max_length=100)
    category    = models.CharField(max_length=100)
    info        = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name