from django.contrib import admin

from .models import Seminar
from .models import City
from .models import Region


admin.site.register(Seminar)
admin.site.register(City)
admin.site.register(Region)
# Register your models here.
