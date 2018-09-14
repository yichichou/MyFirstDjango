from django.contrib import admin
from .models import Post,Record,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Record)
admin.site.register(Category)