from django.urls import path

from App import views

urlpatterns = [
    path('java/<int:name>/', views.name,name='java'),
    # 响应对象
    path('res/',views.hes,name='hes'),

    # 重定向
    path('red/',views.red,name='red'),

#     使用模板引擎
    path('tem/',views.tem,name='tem')
]