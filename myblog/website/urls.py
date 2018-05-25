from django.conf.urls import url
from website.controllers import contact, about, home, file
urlpatterns = [
    url(r'^$', home.index),
    url(r'contact/$', contact.index),
    url(r'about/$', about.index),
    url(r'file/$', file.index),
    url(r'file/submit/$', file.submit),
    url(r'calendar/', file.lich),
]