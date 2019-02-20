from django.contrib import admin
# import models from the model file
from .models import Dog
from .models import Account

admin.site.register(Dog)
admin.site.register(Account)
