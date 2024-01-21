import uuid
import shutil
# Dango
from django.conf import settings
# Users
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Model
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_delete, pre_save


def upload_to(instance: "Note", filename: str) -> str:
    """Путь для файла относительно корня медиа хранилища."""
    return f"{instance.uuid}/{filename}"


class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = "users"


class Tag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to=upload_to, null=True)

    # Relations
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Owner")
    tags = models.ManyToManyField(Tag, related_name="notes", verbose_name="Теги")

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=("created_at",), name="created_at_index"),
            models.Index(fields=("updated_at",), name="updated_at_index"),
        ]


@receiver(post_delete, sender=Note)
def delete_note(sender, instance: Note, **kwargs):
    if instance.image:
        shutil.rmtree((settings.MEDIA_ROOT / str(instance.uuid)))


@receiver(pre_save, sender=Note)
def presave_note(sender, instance: Note, **kwargs):
    if instance.uuid is not None:
        try:
            note = Note.objects.get(uuid=instance.uuid)
        except Note.DoesNotExist:
            note = None

        if note is not None:
            note = Note.objects.get(uuid=instance.uuid)
            if note.image != instance.image:
                shutil.rmtree((settings.MEDIA_ROOT / str(instance.uuid)))
