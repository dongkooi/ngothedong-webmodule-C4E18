from mongoengine import *
#2. Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    description = StringField()
    address = StringField()
    status = BooleanField()
    image = ImageField()
    measurements = ListField()

