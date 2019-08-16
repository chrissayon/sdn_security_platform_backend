from django.contrib import admin
from .models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats
# Register your models here.

class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('last_modified',)

#admin.site.register(Switch, DateAdmin)
admin.site.register(DescStats, DateAdmin)
admin.site.register(FlowStats, DateAdmin)
admin.site.register(FlowAggregateStats, DateAdmin)
admin.site.register(TableStats, DateAdmin)
admin.site.register(PortStats, DateAdmin)
