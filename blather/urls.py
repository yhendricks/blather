from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blat import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.home, name="homepage"),
    url(r'^$', views.IndexView.as_view(), name="homepage"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^my/$', views.MyView.as_view(), name='myview'),
]
