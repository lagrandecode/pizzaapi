from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderCreateListView.as_view()),
    path('<int:pk>/',views.OrderDetailView.as_view(),name='order_detail'),
    path('update/<int:pk>/',views.UpdateOrderStatus.as_view(),name='update_stauts'),
    path('user/<int:pk>/orders/',views.OrderView.as_view(),name='user_orders')
]