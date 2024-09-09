from django.contrib import admin
from backend.models import Article

from django.contrib.auth.models import User

admin.site.register(Article)

# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_superuser']
    