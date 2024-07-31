from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Sites
from django.views.generic.edit import CreateView, DeleteView


# Create your views here.

class SitesListView(ListView):
    model = Sites
    template_name = 'sites_view.html'
    context_object_name = 'sites'


class SitesCreateView(CreateView):
    model = Sites
    template_name = "create_site.html" 
    fields = ['name', 'url',]
    success_url = '/sites/'


class SitesDeleteView(DeleteView):
    model = Sites
    success_url = '/sites/'
    template_name = 'sites_confirm_delete.html'