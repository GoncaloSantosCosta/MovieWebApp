from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Movies
from .models import Reviews
from .models import CastCrew

admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(CastCrew)