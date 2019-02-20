


class InputField():

    def __init__(self,
                max_length):

        self.max_length = max_length

    def get_user_input(self):
        userinput = input("[INPUT]>>> ")
        return userinput[:self.max_length]
    
    def display_input(self):
        print(self.get_user_input())


