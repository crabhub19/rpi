from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Instrument)
admin.site.register(Notice)