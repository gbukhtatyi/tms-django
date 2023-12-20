from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.handlers.wsgi import WSGIRequest

import uuid
from .models import Note


# region Page

def page_home(request):
    all_notes = Note.objects.all()

    return render(
        request,
        "home.html",
        {"notes": all_notes}
    )


def page_about_us(request):
    return render(
        request,
        "pages/about-us.html"
    )


# endregion

# region Notes

def note_create(request: WSGIRequest):
    if request.method == "POST":
        note = Note.objects.create(
            title=request.POST.get("title", False),
            content=request.POST.get("content", False),
        )
        return HttpResponseRedirect("/notes/" + str(note.uuid))

    return render(request, "create_form.html")


def note_view(request: WSGIRequest, note_uuid):
    try:
        note = Note.objects.get(uuid=uuid.UUID(note_uuid))
    except Note.DoesNotExist:
        raise Http404

    if request.method == "POST":
        # Update current note
        return note_update(request, note)
    if request.method == "DELETE":
        # Remove current note
        return note_delete(note)

    return render(
        request,
        "notes/view.html",
        {"note": note}
    )


def note_update(request: WSGIRequest, note: Note):
    note.title = request.POST.get("title", False)
    note.content = request.POST.get("content", False)
    note.save()

    return HttpResponseRedirect("/")


def note_delete(note: Note, note_uuid):
    try:
        note = Note.objects.get(uuid=uuid.UUID(note_uuid))
    except Note.DoesNotExist:
        raise Http404

    note.delete()

    return HttpResponseRedirect("/")

# endregion
