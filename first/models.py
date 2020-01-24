from django.db import models

# Create your models here.
SCALING_CHOICES = (
    ('s', 'Small'),
    ('l', 'Large'),
    ('ln', 'Large(noise cancelling)'),
    ('el', 'Enchance Large')
)


class UploadImg(models.Model):
    Img = models.ImageField(upload_to='images/')
    upscaling = models.CharField(choices=SCALING_CHOICES,
                                 max_length=128, default='el')


def __str__(self):
    return self.upscaling
