from juices.cocktails_generator import *

juices, alc, names = get_data(juices_file, alcohols_file, names_file)
while len(juices) > 0:
    cocktail = generate_random_cocktail(juices, alc, names)
    store_cocktail_to_db(cocktail)
