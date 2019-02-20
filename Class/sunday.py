import datetime

class Tweet():
    def __init__(self,author,content,date=str(datetime.date.today())):
        self.author     = author
        self.date       = date
        self.content    = content
    
    def __str__(self):
        return self.content




########################

class User():
    
    def __init__(self,
                  name,
                 password,
                 email,
                 admin=False,
                 logged_in=False
                 ):
        
        self.name      = name
        self.password  = password
        self.email     = email
        self.admin     = admin
        self.logged_in = logged_in
        
        self.tweets    = []
        print("New user joined!")
        
               
    def login(self):
        u_password = input("What is your password?\n>>>")
        if u_password == self.password:
            self.logged_in = True
            print("logged in, welcome, {}!".format(self.name))
        else:
            print("wrong password")
    
    def logout(self):
        self.logged_in = False
        print("logged out")
        
    def add_tweet(self,tweet):
        my_tweet = Tweet(self.name, tweet)
        self.tweets.append(my_usertweet)
        

my_user = User("Eyal", "mypassword", "eyal.work@chocron.eu", True)


