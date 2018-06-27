from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.address)
id_to_find = "5b2ba7f2bc54f42684b0c46a"
# hera = Service.objects().get(id=id_to_find)
person = Service.objects().with_id(id_to_find)
if person is not None:
    # hera.delete()
    # print(person.name)
    print(person.yob)
    person.update(set__yob= 1995)
    person.reload()
    print(person.yob)

else:
    print("not found")
# print(hera.to_mongo())
