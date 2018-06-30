import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds123981.mlab.com:23981/c4e18-app
host = "ds123981.mlab.com"
port = 23981
db_name = "c4e18-app"
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