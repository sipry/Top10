from django.urls import path, include
from . import views


urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    path('create-list/', views.create_list, name='create_list'),
    path('my-lists/', views.my_lists, name='my_lists'),

]

