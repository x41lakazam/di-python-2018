import random
import faker
from faker import providers
from blog import models, db

fake = faker.Faker()
fake.add_provider(providers.internet)
fake.add_provider(providers.lorem)
fake.add_provider(providers.date_time)

def generate_user():
    user = models.User()
    user.name = fake.name()
    user.email = fake.ascii_email()
    models.UserHandler(user).add_pwd("password")

    print("Created new user {}".format(user))

    return user

def generate_userpost(user):
    post = models.Post()
    post.title = fake.sentence(nb_words=5)
    post.content = fake.text(max_nb_chars=240)
    post.date  = fake.date_time()

    # Add this post to the user posts
    user.posts.append(post)

    # commit database
    return post

def populate(nb):
    for i in range(nb):
        user = generate_user()
        for j in range(random.randint(0,200)):
            generate_userpost(user) 
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()









