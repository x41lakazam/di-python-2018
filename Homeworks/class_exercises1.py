from datetime import datetime

class Restaurant():

    def __init__(self,
                 name,
                foodtype,
                opening_hour,
                closing_hour,
                max_seating,
                phone_n):
        self.name           = name
        self.foodtype       = foodtype
        self.opening_hour   = opening_hour
        self.closing_hour   = closing_hours
        self.max_seating    = max_seating
        self.phone_n        = phone_n

        self.ratings        = []
        self.comments       = []
        self.current_eaters = 0

    def customer_in(self, n):
        if self.current_eaters + n < self.max_seating:
            self.current_eaters += n
        else:
            print("Cant fit so much clients")

    def add_review(self, comment, rating_score):
        if not 0 <= rating_score <= 5:
            print("Please insert a real score between 0 and 5")
            return False

        self.comemnts.append(comment)
        self.ratings.append(rating_score)

    def get_rate(self):
        if len(self.ratings) > 0:
            return sum(self.ratings)/len(self.ratings)
        else:
            return 2.5

    def check_if_open(self):
        current_hour = datetime.now().hour
        if opening_hours <= current_hour < closing_hour:
            return True
        return False

    def __str__(self):
        answer  = ""
        answer += "{} is a {} restaurant that got a rating score of {} \
                ({} people rated it). ".format(self.name,
                                              self.foodtype,
                                              self.get_rate,
                                              len(self.ratings) 
        answer += "It's opened from {}:00 until {}:00. ".format(self.opening_hour,
                                                               self.closing_hour)

        answer += "Currently, there are {} places available to eat there ".format(self.max_seating - self.current_eaters)

        answer += "Contact :{}".format(self.phone_n)


































    


