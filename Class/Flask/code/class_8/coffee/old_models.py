class Coffee:

    id      = 0
    objects = []

    def __init__(self,
                name,
                strength,
                price):

        self.name       = name
        self.strength   = strength
        self.price      = price

        self.id         = Coffee.id
        Coffee.id      += 1

        Coffee.objects.append(self)

    def __repr__(self):
        return "<Coffee {}>".format(self.name)
