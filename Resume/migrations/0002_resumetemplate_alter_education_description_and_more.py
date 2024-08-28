# Generated by Django 5.0.7 on 2024-08-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('template', models.CharField(max_length=100, verbose_name='Шаблон')),
                ('image', models.ImageField(upload_to='template_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Коли ви закінчили там вчитися'),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name',
            field=models.CharField(max_length=250, verbose_name='Назва навчального закладу'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(verbose_name='Коли ви почали там вчитися'),
        ),
        migrations.AlterField(
            model_name='education',
            name='still_studying',
            field=models.BooleanField(default=False, verbose_name='Все ще вчитеся ?'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=250, verbose_name='Назва компанії'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис досвіду'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Коли ви закінчили там працювати'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_title',
            field=models.CharField(max_length=100, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(verbose_name='Коли ви почали там працювати'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='still_work',
            field=models.BooleanField(default=False, verbose_name='Все ще працюєте ?'),
        ),
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[('a1', 'A1'), ('a2', 'A2'), ('b1', 'B1'), ('b2', 'B2'), ('c1', 'C1'), ('c2', 'C2')], default='a1', max_length=5, verbose_name='Ваш рівень'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Назва мови'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Ваш адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Ваш Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name="Ваше ім'я"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Ваше прізвище'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Ваш номер телефону'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Ваш веб-сайт(якщо такий є)'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Назва навичка'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rate',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=1, max_length=5, verbose_name='Наскільки во оцінюєте свій навичок'),
        ),
    ]