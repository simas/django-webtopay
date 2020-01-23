import django

no_patterns = False
if django.VERSION >= (1, 10):
    from django.urls import path
    from webtopay.views import makro
    no_patterns = True
elif django.VERSION >= (1, 6):
    from django.conf.urls import patterns, url
else:
    from django.conf.urls.defaults import patterns, url


if no_patterns:
    urlpatterns = [
        path('', makro, name="webtopay-makro"),
    ]
else:
    urlpatterns = patterns('webtopay.views',
        url(r'^$', 'makro', name="webtopay-makro"),
    )
    
