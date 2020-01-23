from django.contrib import admin

from webtopay.models import WebToPayResponse

class WebToPayResponseAdmin(admin.ModelAdmin):
    list_display = ('timestamp', '__unicode__', 'name', 'surename', 'status',
            'p_email', 'test')

    search_fields = (
        'name',
        'surename',
        'p_email',
    )
    
    list_filter = ('status', 'test')

admin.site.register(WebToPayResponse, WebToPayResponseAdmin)
