from django.contrib import admin
from .models import Profile
from .models import Description


# Register your models here.
admin.site.register(Profile)
admin.site.register(Description)
