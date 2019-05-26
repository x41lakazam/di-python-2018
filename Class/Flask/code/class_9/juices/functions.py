import random


def cocktail_generator(fruits_file, alcohol_file, juices_file):

    juice = {
        'name': None,
        'recipe': []
    }

    fruits = open(fruits_file, 'r').readlines()
    alcohol = open(alcohol_file, 'r').readlines()
    juices = open(juices_file, 'r').readlines()

    juice_name = random.choice(juices).strip()
    alcohol_name = random.choice(alcohol).strip()

    juice['name'] = juice_name
    juice['recipe'].append(alcohol_name)

    for iter in range(3):
        random_ix = random.randrange(0, len(fruits))
        random_fruit = fruits.pop(random_ix).strip()
        juice['recipe'].append(random_fruit)

    return juice


