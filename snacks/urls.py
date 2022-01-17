from django.urls import path
from .views import SnackListView, HomePageView, SnackDetailView


urlpatterns = [
    path('snack_list/',SnackListView.as_view(), name='snack_list'),
    path('snack_detail/<int:pk>/',SnackDetailView.as_view(),name='snack_detail'),
    path('',HomePageView.as_view(), name='home'),
]