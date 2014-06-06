from django.contrib import admin
from django.conf import settings
from logtailer.models import LogFile, Filter

class LogFileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'path')
    
    class Media:
        js = (settings.STATIC_URL+'logtailer/js/jquery.colorbox-min.js',)
        css = {
            'all': (settings.STATIC_URL+'logtailer/css/colorbox.css',)
        }
        
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'regex')   


admin.site.register(LogFile, LogFileAdmin)
admin.site.register(Filter, FilterAdmin)