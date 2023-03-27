from django.urls import path
from .views import HelloAuthView

urlpatterns = [
    path('', views.HelloAuthView.as_view()),
]