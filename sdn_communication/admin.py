from django.contrib import admin
from .models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats 
# Register your models here.

admin.site.register(Switch)
admin.site.register(DescStats)
admin.site.register(FlowStats)
admin.site.register(FlowAggregateStats)
admin.site.register(TableStats)
admin.site.register(PortStats)
