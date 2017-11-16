from django.conf.urls import url

from . import views

app_name = 'heart'
urlpatterns = [

    # /hearts/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dataA>\d+\.\d+)/(?P<dataB>\d+\.\d+)$', views.save, name='save'),

]