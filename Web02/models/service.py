from mongoengine import *
#2. Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     name="XuXu",
#     yob= "1997",
#     gender= 0,
#     height= 153,
#     phone= "01695658921",
#     address= "Sài Gòn",
#     status= False
# )
# new_service.save()