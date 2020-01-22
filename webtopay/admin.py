from django.contrib import admin

from webtopay.models import WebToPayResponse

class WebToPayResponseAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'surename', 'status', 'p_email',
            'test')

    search_fields = (
        'name',
        'surename',
        'p_email',
    )

admin.site.register(WebToPayResponse, WebToPayResponseAdmin)
