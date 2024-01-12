from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from .models import User, Note, Tag


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["preview_image", "title", "column_tags", "created_at", "short_content"]
    search_fields = ["title", "content"]
    date_hierarchy = "updated_at"

    @admin.display(description="Содержимое")
    def short_content(self, obj: Note) -> str:
        return obj.content[:50] + "..."

    @admin.display(description="IMG")
    def preview_image(self, obj: Note) -> str:
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="128" />')
        return "X"

    @admin.display(description="Теги")
    def column_tags(self, obj: Note) -> str:
        tags = list(obj.tags.all())
        text = ""
        for tag in tags:
            text += f"<span style=\"color: blue;\">{tag}</span><br>"
        return mark_safe(text)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["content"]


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
