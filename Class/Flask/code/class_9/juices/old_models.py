class Juice:

    nb_of_juices = 0
    class_objs = []

    def __init__(self, name, recipe):
        """
        Create a Juice object
        :param name: (str) Name of the juice
        :param recipe: (list) List of ingredients
        """
        self.name   = name
        self.recipe = recipe

        self.id     = Juice.nb_of_juices
        Juice.nb_of_juices += 1

        Juice.class_objs.append(self)

    def __repr__(self):
        return "<Juice {}>".format(self.name)

class Store:

    nb_of_stores = 0
    class_objs = []

    def __init__(self, name, location, opening_hours):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours

        self.id  = Store.nb_of_stores
        Store.nb_of_stores += 1

        Store.class_objs.append(self)

    def __repr__(self):
        return "<Store {}>".format(self.name)

