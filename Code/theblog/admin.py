from django.contrib import admin
from .models import Post, Category, Country, City, SentData
# Register your models here.

admin.site.register(Post)

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(SentData)
