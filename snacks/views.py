from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack
# Create your views here.
class SnacksListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnacksDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack