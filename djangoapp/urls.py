from django.conf.urls import url

from djangoapp import views

urlpatterns = [
    url(r'^add_user/', views.add_user),
    url(r'^show_user/', views.show_user),
]