from django.contrib import admin
from controler.models import edits,mod,trend
class editsadmin(admin.ModelAdmin):
    list_display=('News_title','News_dis')
admin.site.register(edits,editsadmin)

class modadmin(admin.ModelAdmin):
    list_display=('mod_title','mod_dis')
admin.site.register(mod,modadmin)

class trendadmin(admin.ModelAdmin):
    list_display=('trend_title1','trend_title2','trend_title3','trend_title4','trend_title5')
admin.site.register(trend,trendadmin)
# Register your models here.
