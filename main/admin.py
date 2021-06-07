from django.contrib import admin
from .models import Moving, JunkRemoval, Consignment

# Register your models here.
admin.site.register(Moving)
admin.site.register(JunkRemoval)
admin.site.register(Consignment)