import modulation as mod

class PasswordInputField(mod.InputField):

    def __init__(self,
                 max_length):
        super().__init__(max_length)

    def display_input(self):
        userinput = self.get_user_input()
        print("*"*len(userinput))


pwd = PasswordInputField(10)
pwd.display_input()
