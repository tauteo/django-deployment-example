from django.conf.urls import url
from basic_app import views

#for template tagging
app_name = 'basic_app' #must equal app name

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
