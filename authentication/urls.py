from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloAuthView.as_view()),
    path('signup/',views.UserCreateView.as_view(), name='signup'),
]