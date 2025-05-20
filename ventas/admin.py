from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ventas.domain.models.user import User

# Register your models here.

admin.site.register(User, UserAdmin)
