from django.conf.urls import patterns, include, url
import pamauth, pimanager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pimanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pamauth.views.login_view'),
    url(r'^login/$', 'pamauth.views.login_view'),
    url(r'^logout/$', 'pamauth.views.logout_view'),
    url(r'^home/$', 'pimanager.views.home'),
)
