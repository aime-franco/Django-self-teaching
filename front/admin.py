from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message # importing the models, to have access to them


# registering the models to admin so that they can be seen on admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)