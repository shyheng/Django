from django.urls import path

from App import views

urlpatterns = [
    # 不能以/开头
    path('home',views.home,name='home')
]