from django.contrib import admin

# Register your models here.

from . import models

class AddressAdmin(admin.ModelAdmin):
    pass

class TrafficAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.TrafficReport, TrafficAdmin)