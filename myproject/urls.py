from django.conf.urls import *  # NOQA
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from mydatabase.views import * 


admin.autodiscover()

#urlpatterns = i18n_patterns('',
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA

    url(r'^$', home.as_view()), 
   
    url('^(?P<page_slug>.*)/$', article.as_view()),
    url('^notfound/$', home.as_view()),
    url(r'^sitemap\.xml$',generate_sitemap),



)


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
