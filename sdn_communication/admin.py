from django.contrib import admin
from .models import Switch, DescStats, FlowStats, FlowAggregateStats, TableStats, PortStats
from .models import PortDiffStats, FlowAggregateDiffStats
from .models import AttackNotification
# Register your models here.

class DateAdmin(admin.ModelAdmin):
    readonly_fields = ('last_modified',)

admin.site.register(Switch)
admin.site.register(DescStats, DateAdmin)
admin.site.register(FlowStats, DateAdmin)
admin.site.register(FlowAggregateStats, DateAdmin)
admin.site.register(PortStats, DateAdmin)
admin.site.register(PortDiffStats, DateAdmin)
admin.site.register(FlowAggregateDiffStats, DateAdmin)
admin.site.register(AttackNotification, DateAdmin)
