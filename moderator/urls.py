from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'moderator.views.index'),
    url(r'^index/$', 'moderator.views.index'),
    url(r'^new_optionset/$', 'moderator.views.new_optionset'),
    url(r'^/$', 'moderator.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/moderator/'}),
    url(r'^signup/$', 'moderator.views.signup'),
    url(r'^optionset/(?P<optionset_id>\d+)/add_options/$', 'moderator.views.add_options'),
)
