from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Note, Tag


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


