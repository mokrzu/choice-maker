from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<registration_id>\w+)$', 'registration.views.index'),
    url(r'^(?P<registration_id>\w+)/(?P<option_id>\w+)/register$', 'registration.views.register'),
    url(r'^(?P<registration_id>\w+)/(?P<option_id>\w+)/save$', 'registration.views.save_choice')
    )
