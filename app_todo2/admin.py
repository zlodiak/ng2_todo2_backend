from django.contrib import admin
from .models import User, Todo, Marker

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Marker)