from django.urls import path

from . import views

urlpatterns = [
    path('', views.TrafficListView.as_view(), name='traffic.list'),
    path('<int:pk>', views.TrafficDetailView.as_view(), name='traffic.detail'),
]