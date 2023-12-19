from django.contrib import admin
from userauths.models import User
#from import_export.admin import Impot_ExportModelAdmin
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']  # List of fields to display in the admin

admin.site.register(User,UserAdmin)
