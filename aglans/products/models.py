from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    images = models.TextField()

@models.permalink
def get_absolute_url(self):
     return ('aglans_products_detail', (),
          {
             'slug': self.slug,
     })
def save(self, *args, **kwargs):
     if not self.slug:
         self.slug = slugify(self.title)
         super(products, self).save(*args, **kwargs)

class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
   # products = models.ForeignKey(products, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
