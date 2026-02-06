from django.contrib import admin
from .models import  CompanyDetails, SignalDetails,VideoDetails

# Register your models here.
admin.site.register(CompanyDetails)
admin.site.register(SignalDetails)
admin.site.register(VideoDetails)

