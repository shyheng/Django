from django.urls import path

from App import views

urlpatterns = [
    path('shy/',views.test,name='test'),
]