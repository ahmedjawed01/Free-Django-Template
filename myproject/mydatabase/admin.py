from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

class CommonMedia:
    css = {
            "all": ("/static/editor.css",)
        }
    js = ("/static/editor.js",'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',)




class PagesAdmin(admin.ModelAdmin):
    Media=CommonMedia
    search_fields = ('title',)
    list_display = ('title','id','slug_link')
    
    #formfield_overrides = {
        
        #models.TextField: {'widget': Textarea(attrs={'rows':100, 'cols':100})},
    #}
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    class Media:
        js = ('ckeditor/ckeditor.js',)
admin.site.register(Pages,PagesAdmin)




    
        




class SetingsAdmin(admin.ModelAdmin):

    search_fields = ('title',)
    list_display = ('title',)
    
        
    actions = None



admin.site.register(Settings,SetingsAdmin)



