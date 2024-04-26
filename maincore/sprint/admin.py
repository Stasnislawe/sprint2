from django.contrib import admin
from .models import User, DifficultyLevel, Coords, AddMount, Images

# Register your models here.

admin.site.register(User)
admin.site.register(DifficultyLevel)
admin.site.register(Coords)
admin.site.register(AddMount)
admin.site.register(Images)