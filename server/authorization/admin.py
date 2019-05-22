from django.contrib import admin
from app01.models import Tbluserinfo

# Register your models here.

# admin.site.register(User)


@admin.register(Tbluserinfo)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['open_id']
