from django.conf.urls import url
from website.controllers import contact, about, home, file
urlpatterns = [
    url(r'^$', home.index),
    url(r'contact/$', contact.contact),
    url(r'about/$', about.about),
    url(r'file/$', file.index),
    url(r'file/submit/$', file.submit),
]