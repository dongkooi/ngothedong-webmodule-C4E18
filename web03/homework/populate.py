import mlab
from models.service import Service
from faker import Faker
from random import choice, randint

mlab.connect()

fake = Faker()
# print(fake.address())
new_service = Service(
    name = "XuXu",
    yob = 1997,
    gender = 0,
    height = 153,
    phone = "0123456789",
    description = "ngoan hiền, dễ thương, lễ phép với gia đình, ...",
    image = "static/image/xuxu.jpg",
    address = "Nam Định",
    status = False,
    measurements = [80,68,85]
)
new_service.save()