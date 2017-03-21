from django.conf.urls import url
from patron_password_app import views


app_name = 'patron_password_app'


urlpatterns = [
    url(r'^search', views.search, name='search'),
    url(r'^patron/(?P<patron_number>[0-9]+)/$',views.patron_view, name = 'patron_view'),
    url(r'^patronedit/(?P<patron_number>[0-9]+)/$',views.patron_edit, name = 'patron_edit'),
    url(r'^patronadd',views.patron_add, name = 'patron_add'),
    url(r'^patrondelete/(?P<patron_number>[0-9]+)/$',views.patron_delete, name = 'patron_delete'),
]
