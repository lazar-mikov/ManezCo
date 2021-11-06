from django.contrib import admin
from .models import Adult, User, Child, Admin

admin.site.register(User)
admin.site.register(Adult)
admin.site.register(Child)
admin.site.register(Admin)
