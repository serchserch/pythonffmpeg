from django.conf.urls import patterns, include, url

from devices import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'viveclaro5.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^videomp4/', views.videomp4, name='videomp4'),
    url(r'^videoogg/', views.videoogg, name='videoogg'),
    url(r'^videowebm/', views.videowebm, name='videowebm'),
    url(r'^login/', views.login, name='login'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^viveclaro5/', include(viveclaro5.urls)),
)
