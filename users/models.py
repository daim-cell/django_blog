from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username}'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if (img.height >300 or img.width >300):
             img.thumbnail((600,600))
             img.save(self.image.path)

