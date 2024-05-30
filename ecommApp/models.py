from django.db import models

# Create your models here.
class CarouselProduct(models.Model):
    img = models.ImageField(upload_to='carousel', verbose_name=''),
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name