from django import forms
from .models import Ingredient


class IngredientForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and Ingredient.objects.filter(title=title).exists():
            raise forms.ValidationError('Ingredient with the same title already exists')

        return title

    class Meta:
        model = Ingredient
        fields = [
            "title",
            "content",
            "calories"
        ]
