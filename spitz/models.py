from django.db import models
from django.urls import reverse

class Spitz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    typeS = models.ForeignKey("TypesSpitz", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class TypesSpitz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})    