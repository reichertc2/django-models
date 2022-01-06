from typing import Generic
from django.views.generic import TemplateView,ListView,DetailView


class SnackListView(DetailView):
    template_name = 'snack_list.html'