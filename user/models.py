from django.db import models

# from django.contrib.auth.models import AbstractUser



# class CustomUser(AbstractUser):
#     GENDERS = (
#         ('m', 'male'),
#         ('f', 'female'),
#     )

#     fio = models.CharField('FIO', max_length=100)
#     gender = models.CharField('Gender', max_length=1, choices=GENDERS)
#     birth_date = models.DateField('Birth date')
#     email = models.EmailField()


# class Teamers(models.Model):
#     name = models.CharField(max_length=100)


# """
# 6.1.3 Model inheritence in Practice: The TimeStampedModel
# """

# class TimeStampModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
