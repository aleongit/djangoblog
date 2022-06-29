from django.contrib import admin
from .models import Post, Valoracio

admin.site.register([
    Post,
    Valoracio
])
