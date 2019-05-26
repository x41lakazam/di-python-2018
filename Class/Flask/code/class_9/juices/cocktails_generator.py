import random
from juices import db, models

juices_file   = "juices/juices_names.txt"
alcohols_file = "juices/alcohol_names.txt"
fruits_file   = "juices/fruits_names.txt"

class Cocktail:
    def __init__(self, name, alcohol, fruit1, fruit2, fruit3):
        self.name = name
        self.build_recipe(alcohol, fruit1, fruit2, fruit3)

    def build_recipe(self, alcohol, fruit1, fruit2, fruit3):
        self.recipe = ', '.join([alcohol, fruit1, fruit2, fruit3])
    
    def __repr__(self):
        return "<Cocktail {} - {}>".format(self.name, self.recipe)


def filter_file_data(lines):
    clean_lines = []
    for line in lines:
        line = line.strip()
        if len(line):
            clean_lines.append(line.title())

    return clean_lines

def get_data(juices_file, alc_file, fruits_file):

    juices = filter_file_data(open(juices_file, 'r').readlines())
    fruits = filter_file_data(open(fruits_file, 'r').readlines())
    alcohols = filter_file_data(open(alcohols_file, 'r').readlines())

    return juices, fruits, alcohols

def generate_random_cocktail(juices, fruits, alc):
    """
    generating a random cocktail with:
    A random name
    Three random fruits and one random alcohol
    """
    fruits_cpy = fruits.copy()

    # Pick a name
    name = random.choice(juices)
    juices.remove(name)

    # Pick an alcohol
    alcohol = random.choice(alc)

    # Pick three fruits
    fruit1  = random.choice(fruits_cpy)
    fruits_cpy.remove(fruit1)

    fruit2  = random.choice(fruits_cpy)
    fruits_cpy.remove(fruit2)

    fruit3  = random.choice(fruits_cpy)
    fruits_cpy.remove(fruit3)

    cocktail = Cocktail(name, alcohol, fruit1, fruit2, fruit3)

    return cocktail

def store_cocktail_to_db(cocktail):
    juice_obj = models.Juice(name=cocktail.name,
                     recipe=cocktail.recipe)

    db.session.add(juice_obj)
    db.session.commit()

    print("Added {} to db".format(juice_obj))

def populate_cocktails(juices_file, alc_file, fruits_file):
    juices, alc, fruits = get_data(juices_file, fruits_file, alc_file)

    while len(juices) > 0:
        cocktail = generate_random_cocktail(juices, fruits, alc)
        store_cocktail_to_db(cocktail)

    return True

