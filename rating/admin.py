from django.contrib import admin
from .models import Deputy


admin.site.site_header = 'Young Deputies Rating'

admin.site.register(Deputy)
