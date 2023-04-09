from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderCreateListView.as_view()),
    path('<int:pk>/',views.OrderDetailView.as_view(),name='order_detail')
]