from django.contrib import admin

# Register your models here.
from .models import Post,Owner

admin.site.register(Post)
admin.site.register(Owner)