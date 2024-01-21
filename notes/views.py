import uuid
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import User, Note
from .services import get_user_tags


# region Auth

def auth_register(request: WSGIRequest):
    if request.method != "POST":
        return render(request, "auth/register.html")

    if (not request.POST.get("username")
            or not request.POST.get("email")
            or not request.POST.get("password")
            or not request.POST.get("password_confirm")):
        return render(
            request,
            "auth/register.html",
            {"errors": ["Please enter all fields!"]}
        )

    errors = []

    user_name = request.POST["username"]
    user_email = request.POST["email"]
    user_password = request.POST["password"]
    user_password_confirm = request.POST["password_confirm"]

    if User.objects.filter(
            Q(username=user_name) | Q(email=user_email)
    ).count() > 0:
        errors.append("A user with the same name or email address already exists")

    if user_password != user_password_confirm:
        errors.append("Password mismatch")

    if len(errors) > 0:
        return render(
            request,
            "auth/register.html",
            {"errors": errors}
        )

    User.objects.create_user(
        username=user_name,
        email=user_email,
        password=user_password
    )

    return HttpResponseRedirect("/")


# endregion

# region Page

def page_home(request):
    search = request.GET.get('search', '')

    if search:
        all_notes = Note.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
    else:
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


# region Users

@login_required
def user_profile(request: WSGIRequest):
    errors = []
    if request.method == "POST":
        request.user.first_name = request.POST.get("firstname", None)
        request.user.last_name = request.POST.get("lastname", None)
        request.user.phone = request.POST.get("phone", None)
        request.user.save()

    tags = get_user_tags(request.user.id)

    return render(request, "users/profile.html", {
        "tags": tags,
        "errors": errors
    })


def user_notes(request: WSGIRequest, username):
    try:
        owner = User.objects.get(username=username)
    except Note.DoesNotExist:
        return render(request, "home.html", {"errors": ["User not found."]})

    return render(request, "users/notes.html", {
        "owner": owner,
        "notes": Note.objects.filter(user_id=owner.id)
    })


# endregion

# region Notes

@login_required
def note_create(request: WSGIRequest):
    if request.method == "POST":
        note = Note.objects.create(
            title=request.POST.get("title", False),
            content=request.POST.get("content", False),
            user=request.user,
            image=request.FILES.get("image", None)
        )
        return HttpResponseRedirect("/notes/" + str(note.uuid))

    return render(request, "create_form.html")


@login_required
def note_view(request: WSGIRequest, note_uuid):
    try:
        note = Note.objects.get(uuid=uuid.UUID(note_uuid))
    except Note.DoesNotExist:
        raise Http404

    if request.user != note.user:
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
    note.image = request.FILES.get("image", note.image)
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
