import uuid
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .models import Ingredient
from .forms import IngredientForm


def food_index(request: WSGIRequest):
    form = IngredientForm()
    all_ingredients = Ingredient.objects.all()

    return render(
        request,
        "food/index.html",
        {
            "ingredients": all_ingredients,
            "form": form
        }
    )


@login_required
def ingredient_create(request: WSGIRequest):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = Ingredient.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                calories=form.cleaned_data['calories'],
            )

            return HttpResponseRedirect("/food/ingredients/" + str(ingredient.uuid))

    return HttpResponseRedirect("/food")


def ingredient_update(request: WSGIRequest, ingredient_uuid):
    try:
        ingredient = Ingredient.objects.get(uuid=uuid.UUID(ingredient_uuid))
    except Ingredient.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient: Ingredient = form.save()

            return HttpResponseRedirect("/food/ingredients/" + str(ingredient.uuid))
    else:
        form = IngredientForm(instance=ingredient)

    return render(
        request,
        "food/ingredient/view.html",
        {
            "ingredient": ingredient,
            "form": form
        }
    )
