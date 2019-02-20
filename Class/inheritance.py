class Car():

    def __init__(self,
                year,
                model):
        
        self.model      = model
        self.year       = year

        self.odometer   = 0

    def description(self):
        print("This is a {} from {}".format(self.model, self.year))

    def turn_on(self):
        print("VROOM")

class ElectricCar(Car):

    def __init__(self,
                 year,
                 model,
                 voltage):

        super().__init__(year,model)
        self.voltage = voltage


    def turn_on(self):
        print("...")


#my_tesla = ElectricCar(2014, "tesla", 400)
#my_tesla.turn_on()




























