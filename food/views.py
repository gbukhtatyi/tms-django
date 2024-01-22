from django.shortcuts import render, get_object_or_404
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
                name=form.cleaned_data['name'],
                content=form.cleaned_data['content'],
                calories=form.cleaned_data['calories'],
            )

            return HttpResponseRedirect("/food/ingredients/" + str(ingredient.id))

    return HttpResponseRedirect("/food")


def ingredient_update(request: WSGIRequest, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient: Ingredient = form.save()

            return HttpResponseRedirect("/food/ingredients/" + str(ingredient.id))
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
