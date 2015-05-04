from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='polls'),
    # ex: /polls/5/
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
]