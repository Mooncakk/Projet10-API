from django.contrib import admin
from django.contrib.auth.models import Group


from accounts.models import CustomUser


# Register your models here.
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):

    fields = ['email', 'first_name', 'last_name', 'password', 'is_admin', 'is_staff', 'is_active', ]
    list_display = ('email', 'first_name', 'last_name', 'last_login')


admin.site.register(CustomUser, UserAdmin)
