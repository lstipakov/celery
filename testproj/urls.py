from django.conf.urls.defaults import patterns, url, include, handler500
from celery.views import apply

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^testproj/', include('testproj.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    url(r"^apply/(?P<task_name>.+?)/(?P<args>.+)", apply,
        name="celery-apply"),
    url(r"^celery/", include("celery.urls")),

)