from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$',views.index),
    url('contact/$', views.contact),
    url('about/$',views.about),
]