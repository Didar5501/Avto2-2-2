from django.contrib import admin
from .models import mcfcarbrand, mcfcarmodel

@admin.register(mcfcarbrand)
class McfcarbrandAdmin(admin.ModelAdmin):
    list_display=[ 
                    'id', 
                    'uid', 
                    'Name',
                    'idbs', 
                    'country' ,
                    'creationdate' ,
                    'creationauthor' ,
                    'changedate' ,
                    'changeauthor' ,
                    'mcfcode',
                ]
    readonly_fields=[
                     'creationdate',
                     'changedate'

                ]

@admin.register(mcfcarmodel)
class McfcarmodelAdmin(admin.ModelAdmin):
    list_display=[ 
                    'id', 
                    'uid', 
                    'Name',
                    'idbs', 
                    'creationdate' ,
                    'creationauthor' ,
                    'changedate' ,
                    'changeauthor' ,
                    'mcfcode',
                ]
    readonly_fields=[
                     'creationdate',
                     'changedate'

                ]