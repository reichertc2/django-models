from django.urls import path
from .views import SnackListView, HomePageView


urlpatterns = [
    path('snack_list/',SnackListView.as_view(), name='snack_list'),
    path('',HomePageView.as_view(), name='home'),
]