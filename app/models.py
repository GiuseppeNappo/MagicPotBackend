from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_recipe = db.Column(db.String(64), unique=True)
    decr = db.Column(db.String)
    image = db.Column(db.String)
    difficulty = db.Column(db.String)


    def __repr__(self):
        return '<Recipe {}>'.format(self.name_recipe)


class Ingredient(db.Model):
    name = db.Column(db.String(64), primary_key=True, unique = True)

    def __repr__(self):
        return '<Ingredient {}>'.format(self.name)


class Ricin(db.Model):
    code = db.Column(db.Integer , primary_key=True)
    name_i = db.Column(db.String(64), db.ForeignKey('ingredient.name'), primary_key=True)
    idr = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    quantity = db.Column(db.String(64))

    def __repr__(self):
        return '<Ricin {}>'.format(self.name_i)
