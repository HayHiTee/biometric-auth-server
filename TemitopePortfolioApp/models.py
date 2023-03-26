from django.db import models
from PIL import Image
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return str(self.username)


def user_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cats/<path_to_function>
    return 'cats/{0}'.format(filename)


class Cat(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=user_image_directory_path)


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

