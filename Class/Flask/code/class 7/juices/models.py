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


