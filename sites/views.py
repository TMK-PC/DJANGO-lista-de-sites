from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Sites
from django.views.generic.edit import CreateView, DeleteView


# Create your views here.

class SitesListView(ListView):
    model = Sites
    template_name = 'sites_view.html'
    context_object_name = 'sites'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', '')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class SitesCreateView(CreateView):
    model = Sites
    template_name = "create_site.html" 
    fields = ['name', 'url', 'icon',]
    success_url = '/sites/'


class SitesDeleteView(DeleteView):
    model = Sites
    success_url = '/sites/'
    template_name = 'sites_confirm_delete.html'