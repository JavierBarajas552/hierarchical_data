from django.contrib import admin
from .models import Folder
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
admin.site.register(Folder, DraggableMPTTAdmin)
