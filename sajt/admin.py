from django.contrib import admin
from .models import *

models = [News, Category, Event, Lecturer, Subscriber, Participant]
admin.site.register(models)
