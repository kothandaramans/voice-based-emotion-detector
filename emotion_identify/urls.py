from django.conf.urls import include, url
from emotion_identify import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'image_share.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.upload, name = "main"),
    url(r'^handl/$', views.hnd_load, name = "handl"),
    url(r'^record/$',views.recording, name="record"),
    url(r'^sample/(?P<value>\d+)/.*$', views.sample, name="sample"),
]
