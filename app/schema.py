from app.models import Recipe, Ingredient
from app import ma


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe

class TitleRecipeSchema(ma.Schema):
    class Meta:
        fields = ('name_recipe','id')


class IngredientSchema(ma.Schema):
    class Meta:
        fields = ('name_i', 'quantity')

class FullIngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient