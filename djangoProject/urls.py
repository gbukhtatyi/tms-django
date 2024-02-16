"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import notes.views
import food.views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Auth
    path('auth/', include("django.contrib.auth.urls")),
    path('auth/register', notes.views.auth_register),

    # Pages
    path("", notes.views.page_home),
    path("about-us", notes.views.page_about_us),

    # Users
    path("profile", notes.views.user_profile),
    path("user/<username>/notes", notes.views.user_notes),

    # Notes
    path("notes", notes.views.note_create),
    path("notes/latest", notes.views.note_latest, name="note-latest"),
    path("notes/<note_uuid>", notes.views.note_view, name="note-view"),
    path("notes/<note_uuid>/remove", notes.views.note_delete),

    # Food
    path("food", food.views.food_index),
    path("food/ingredients", food.views.ingredient_create),
    path("food/ingredients/<ingredient_id>", food.views.ingredient_update),

    # API - Auth
    path('api/auth/', include('djoser.urls.authtoken')),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/auth/", include("djoser.urls.base")),

    # API
    path('api/notes', include('notes.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
