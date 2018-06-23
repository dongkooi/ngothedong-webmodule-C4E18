from mongoengine import *
#2. Design database
class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() 
    phone = StringField()
    email = StringField()
    address = StringField()  
    job = StringField()
    company = StringField()
    contacted = BooleanField()

# new_service.save()