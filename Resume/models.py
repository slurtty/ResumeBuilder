from django.db import models
from django.contrib.auth.models import AbstractUser




class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    still_work = models.BooleanField(default=False)


    def __str__(self):
        return self.job_title


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.institution_name


class Skill(models.Model):

    RATE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rate = models.CharField(max_length=5, choices=RATE_CHOICES, default=1)

    def __str__(self):
        self.name


class Language(models.Model):
    LEVEL_CHOICES = [
        ('a1', 'A1'),
        ('a2', 'A2'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('c1', 'C1'),
        ('c2', 'C2'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES, default='a1')

    def __str__(self):
        self.name