from mongoengine import *

#1. Design database
class Video(Document):
    title = StringField()
    thumbnail = StringField()
    link = StringField()
    views = IntField()
    youtube_id = StringField()