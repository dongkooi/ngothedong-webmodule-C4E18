import mlab
from models.customer import Customer
from faker import Faker
from random import choice, randint

mlab.connect()

fake = Faker()

for i in range(20):
    print("Saving customer", i + 1, "...")
    new_customer = Customer(
        name= fake.name(),
        yob= randint(1990, 2000),
        gender= randint(0, 1),
        phone= fake.phone_number(),
        email= fake.email(),
        address= fake.address(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )
    new_customer.save()