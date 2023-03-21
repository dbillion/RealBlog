from django.db import models
from taggit.managers import TaggableManager
from django_filters import FilterSet, filters
import django_filters
from PIL import Image
# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=70)
    contents = models.TextField()
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(default='', blank=True, upload_to='images')
    tag = TaggableManager(blank=True)
    thumbnail = models.ImageField(default='default_thumbnail.jpg',upload_to='thumbnails/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    def __int__(self):
        return self.postname

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url






class Owner(models.Model):
    postname = models.CharField(max_length=70)
    contents = models.TextField()
    image = models.ImageField(default='', blank=True, upload_to='images')


    def __int__(self):
        return self.postname

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['postname', 'contents']
        # filter_overrides = {
        #     TaggableManager: {
        #         'filter_class': filters.CharFilter,
        #         'extra': lambda f: {
        #             'lookup_expr': 'exact',
        #         },
        #     },
        # }
