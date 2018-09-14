from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^trends$', views.trends, name='trends'),
]
