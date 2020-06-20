from __future__ import print_function
import json
from flask import jsonify, request, Response
from flask_mail import Message
from app import mail
from app import app
from app.lsa import LSA
from app.models import Recipe, Ricin, Ingredient
from app.schema import RecipeSchema, IngredientSchema, FullIngredientSchema, TitleRecipeSchema
import uuid

recipeSchema = RecipeSchema()
ingredientSchema = IngredientSchema(many=True)
fullIngredientSchema = FullIngredientSchema(many=True)
titleRecipeSchema = TitleRecipeSchema(many=True)


@app.route('/lsa', methods=['POST'])
def getRecipes():
    fullRecipe = []
    ingredients = request.get_json()
    indexes = (LSA.lsa(ingredients[0]['Ingredients']))
    for q in range(len(indexes)):
        resultQueryRecipe = Recipe.query.filter_by(id=int(indexes[q])).first()
        resultQueryIngredients = Ricin.query.filter_by(idr=int(indexes[q])).all()
        dicRecipeSchema = recipeSchema.dump(resultQueryRecipe)
        dicIngredientsSchema = ingredientSchema.dump(resultQueryIngredients)
        dicRecipeSchema['Ingredients'] = dicIngredientsSchema
        fullRecipe.append(dicRecipeSchema)

    return Response(json.dumps(fullRecipe), mimetype='application/json')


@app.route('/mail', methods=['POST'])
def sendMail():
    message = request.get_json()
    msg = Message(str(uuid.uuid1()), sender='provamandatario@gmail.com', recipients=['provaricevente@gmail.com'])
    msg.body = str(message)
    mail.send(msg)

    return jsonify({"message": "Messaggio Inviato"})


@app.route('/allIngredients', methods=['GET'])
def allIngredients():
    variabile = {}
    fullIngredientsQuery = Ingredient.query.all()
    dicIngredientSchema = fullIngredientSchema.dump(fullIngredientsQuery)
    variabile['dict'] = dicIngredientSchema

    return Response(json.dumps(variabile), mimetype='application/json')

@app.route('/allRecipe', methods=['GET'])
def allTitleRecipe():
    titleRecipe = Recipe.query.all()
    dicRecipeSchema =titleRecipeSchema.dump(titleRecipe)

    return Response(json.dumps(dicRecipeSchema), mimetype='application/json')

@app.route('/allRecipe/<string:title>', methods=['GET'])
def titleRecipe(title):
    fullRecipe = []
    resultQueryRecipe = Recipe.query.filter_by(name_recipe=title).first()
    dicRecipeSchema = recipeSchema.dump(resultQueryRecipe)
    idr = dicRecipeSchema['id']
    resultQueryIngredients = Ricin.query.filter_by(idr=idr).all()
    dicIngredientsSchema = ingredientSchema.dump(resultQueryIngredients)
    dicRecipeSchema['Ingredients'] = dicIngredientsSchema
    fullRecipe.append(dicRecipeSchema)
    return Response(json.dumps(fullRecipe), mimetype='application/json')

@app.route('/allRecipe/<int:page>', methods=['GET'])
def allRecipes(page):
    fullRecipe = []
    Range = page * 10 - 10
    toRange = Range + 10

    for i in  range(Range,toRange):
        resultQueryRecipe = Recipe.query.filter_by(id=i).first()
        resultQueryIngredients = Ricin.query.filter_by(idr=i).all()
        dicRecipeSchema = recipeSchema.dump(resultQueryRecipe)
        dicIngredientsSchema = ingredientSchema.dump(resultQueryIngredients)
        dicRecipeSchema['Ingredients'] = dicIngredientsSchema
        fullRecipe.append(dicRecipeSchema)

    return Response(json.dumps(fullRecipe), mimetype='application/json')