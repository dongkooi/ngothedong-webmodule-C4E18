from models.service import Service
import mlab

mlab.connect()


all_service = Service.objects()
for service in all_service:
    service.delete()