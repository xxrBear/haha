from django.conf.urls import url

from user import views


urlpatterns = [
   url('rawqueryset', views.test_rawqueryset)
]
