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
    products = models.ForeignKey('products', on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)

#class Blog(models.Model):
#    title = models.CharField(max_length=255)
#    content = models.TextField()
#    created_on = models.DateTimeField(auto_now_add=True)
#    author = models.TextField()
#    images = models.TextField()
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE,)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE,)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
from djangocms_text_ckeditor.fields import HTMLField

from shop.money.fields import MoneyField
from shop.models.product import BaseProduct, BaseProductManager, CMSPageReferenceMixin
from shop.models.defaults.mapping import ProductPage, ProductImage
from shop.models.defaults.order import Order

from ..manufacturer import Manufacturer
class SmartCard(CMSPageReferenceMixin, BaseProduct):
    # common product fields
    product_name = models.CharField(
        _("Product Name"),
        max_length=255
    )

    slug = models.SlugField(_("Slug"))

    unit_price = MoneyField(
        _("Unit price"),
        decimal_places=3,
        help_text=_("Net price for this product"),
    )

    caption = HTMLField(
        _("Caption"),
        configuration='CKEDITOR_SETTINGS_CAPTION',
        help_text=_("Short description used in the catalog's list view of products."),
    )

    images = models.ManyToManyField(
        'filer.Image',
        through=ProductImage,
    )
    # product properties
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name=_("Manufacturer")
    )

    card_type = models.CharField(
        _("Card Type"),
        choices=(2 * ('{}{}'.format(s, t),)
                 for t in ('SD', 'SDXC', 'SDHC', 'SDHC II') for s in ('', 'micro ')),
        max_length=15,
    )

    speed = models.CharField(
        _("Transfer Speed"),
        choices=((str(s), "{} MB/s".format(s))
                 for s in (4, 20, 30, 40, 48, 80, 95, 280)),
        max_length=8,
    )

    product_code = models.CharField(
        _("Product code"),
        max_length=255,
        unique=True,
    )

    storage = models.PositiveIntegerField(
        _("Storage Capacity"),
        help_text=_("Storage capacity in GB"),
    )
     # controlling the catalog
    order = models.PositiveIntegerField(
        _("Sort by"),
        db_index=True,
    )

    cms_pages = models.ManyToManyField(
        'cms.Page',
        through=ProductPage,
        help_text=_("Choose list view this product shall appear on."),
    )
