from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(staffs)
admin.site.register(section)
admin.site.register(students)
admin.site.register(login_info)
# admin.site.register(Student_register_login)
# admin.site.register(Staff_register_login)