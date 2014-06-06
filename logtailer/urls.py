from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('logtailer.views',
    url(r'^readlogs/$', 'read_logs'),
    url(r'^get-log-line/(?P<file_id>\d+)/$', 'get_log_lines', name='logtailer_get_log_lines'),
    url(r'^get-history/(?P<file_id>\d+)/$', 'get_log_lines', {'history': True}, name='logtailer_get_history'),
    url(r'^add-log/$', 'add_log'),
    url(r'^add-filter/$', 'add_filter'),
    url(r'^select-log/$', 'log_select'),
)
