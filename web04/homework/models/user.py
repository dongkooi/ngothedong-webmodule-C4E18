from mongoengine import *
#2. Design database
class User(Document):
    username = StringField()
    password = StringField()
    email = StringField(required=True)
    fullname = StringField(required=True)

