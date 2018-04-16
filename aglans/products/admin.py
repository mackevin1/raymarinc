from django.contrib import admin

# Register your models here.
from django.contrib import admin
from products.models import Products
from products.models import Comment
from product.models import Blog
admin.site.register(Products)
admin.site.register(Comment)
admin.site.register(Blog)
