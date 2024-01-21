from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "fio", "notes", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": ("first_name", "last_name", "phone", "email")
            }
        ),
    )

    actions = ["block", "unblock"]

    def fio(self, obj: User):
        result = " ".join([obj.first_name, obj.last_name])

        return result if len(result) > 0 else "N/A"

    def notes(self, obj: User):
        amount = Note.objects.filter(user_id=obj.id).count()

        return str(amount)

    @admin.action(description="Block Users")
    def block(self, form, queryset):
        queryset.update(is_active=False)

    @admin.action(description="Unblock Users")
    def unblock(self, form, queryset):
        queryset.update(is_active=True)
