from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.
class SnacksListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnacksDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

class SnacksCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields=['name','purchaser','description']

class SnacksUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields=['name','purchaser','description']
    success_url=reverse_lazy('snack_list')

class SnacksDeleteView(DeleteView):
    pass