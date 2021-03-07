from django.contrib import admin
from .models import Post, Category, Country, City
# Register your models here.

admin.site.register(Post)

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(City)
