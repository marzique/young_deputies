from django.contrib import admin
from .models import Deputy, UniqueUser


admin.site.site_header = 'Young Deputies Rating'

admin.site.register(Deputy)
admin.site.register(UniqueUser)
