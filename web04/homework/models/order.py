from mongoengine import *
#2. Design database
class Order(Document):
    service_id = StringField()
    id_user = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()
