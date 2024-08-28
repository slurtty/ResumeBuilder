from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles' )
    first_name = models.CharField(max_length=100, verbose_name="Ваше ім'я")
    last_name = models.CharField(max_length=100, verbose_name='Ваше прізвище')
    email = models.EmailField(verbose_name='Ваш Email')
    phone = models.CharField(max_length=20, verbose_name='Ваш номер телефону')
    address = models.TextField(blank=True, null=True, verbose_name='Ваш адрес')
    site = models.URLField(blank=True, null=True, verbose_name='Ваш веб-сайт(якщо такий є)')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')
    job_title = models.CharField(max_length=100, verbose_name='Посада')
    company_name = models.CharField(max_length=250, verbose_name='Назва компанії')
    description = models.TextField(blank=True, null=True, verbose_name='Опис досвіду')
    start_date = models.DateField(verbose_name='Коли ви почали там працювати')
    end_date = models.DateField(blank=True, null=True, verbose_name='Коли ви закінчили там працювати')
    still_work = models.BooleanField(default=False, verbose_name='Все ще працюєте ?')


    def __str__(self):
        return self.job_title


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    institution_name = models.CharField(max_length=250, verbose_name='Назва навчального закладу')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    start_date = models.DateField(verbose_name='Коли ви почали там вчитися')
    end_date = models.DateField(blank=True, null=True, verbose_name='Коли ви закінчили там вчитися')
    still_studying = models.BooleanField(default=False, verbose_name='Все ще вчитеся ?')


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

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100, verbose_name='Назва навичка')
    rate = models.CharField(max_length=5, choices=RATE_CHOICES, default=1, verbose_name='Наскільки во оцінюєте свій навичок')

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

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=100, verbose_name='Назва мови')
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES, default='a1', verbose_name='Ваш рівень')

    def __str__(self):
        self.name


class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    template = models.CharField(max_length=100, verbose_name='Шаблон')
    image = models.ImageField(upload_to='template_images/')




