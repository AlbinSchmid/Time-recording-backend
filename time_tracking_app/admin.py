from django.contrib import admin
from .models import StaffName, Project, TimeRecord


admin.site.register(StaffName)
admin.site.register(Project)
admin.site.register(TimeRecord)
