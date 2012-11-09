from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sample_project.views.blocking'),
    url(r'^nonblocking/$', 'sample_project.views.nonblocking'),
    url(r'^slow_and_manualkey/$', 'sample_project.views.slow_and_manualkey'),
    # url(r'^sample_project/', include('sample_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
