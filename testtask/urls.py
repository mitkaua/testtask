from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testtask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'song.views.song_list', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
