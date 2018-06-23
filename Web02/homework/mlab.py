import mongoengine

# mongodb://admin:admin123@ds163330.mlab.com:63330/muadongkhonglanh-c4e18

host = "ds163330.mlab.com"
port = 63330
db_name = "muadongkhonglanh-c4e18"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())