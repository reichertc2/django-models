from django.urls import path
from .views import SnackListView


urlpatterns = [
    path('snack_list/',SnackListView.as_view(), name='snack_list'),
]