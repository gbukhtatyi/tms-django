from django import forms
from .models import Ingredient


class IngredientForm(forms.ModelForm):
    def clean_title(self):
        name = self.cleaned_data.get('name')
        if name and Ingredient.objects.filter(name=name).exists():
            raise forms.ValidationError('Ingredient with the same title already exists')

        return name

    class Meta:
        model = Ingredient
        fields = [
            "name",
            "content",
            "calories"
        ]
