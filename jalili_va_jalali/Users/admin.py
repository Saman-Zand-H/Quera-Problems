from Users.models import CustomUser
from django.contrib import admin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", 
                    "first_name", 
                    "last_name", 
                    "gender", 
                    "national_code", 
                    "birthday_date")
    search_fields = ["username", "full_name"]
    ordering = ("ceremony_datetime", )

    def first_name(self, obj):
        return obj.full_name.split(" ")[0]

    def last_name(self, obj):
        return obj.full_name.split(" ")[1]
