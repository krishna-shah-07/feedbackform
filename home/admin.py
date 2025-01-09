from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(CustomerFeedback)
admin.site.register(CustomerResponse)