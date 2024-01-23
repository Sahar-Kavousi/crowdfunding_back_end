from django.contrib import admin

from .models import CustomUser


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username"]

    @admin.display(empty_value="???")
    def view_brith_day(self, obj):
        return obj.pub_date


admin.site.register(CustomUser,CustomUserAdmin)