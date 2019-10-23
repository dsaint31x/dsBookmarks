from django.db import models

# Create your models here.
from django.urls import reverse
class Bookmark(models.Model):

    site_name = models.CharField(max_length=300)
    url = models.URLField('site url')

    def __str__(self):
        return "이름 : "+self.site_name+", url : "+self.url

    def get_absolute_url (self):
        return reverse('bookmark:detail', args=[str(self.id),])

