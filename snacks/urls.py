from django.urls import path
from .views import SnacksListView, SnacksDetailView
urlpatterns = [
    path('',SnacksListView.as_view(),name='snack_list'),
    path('<int:pk>/',SnacksDetailView.as_view(),name='snack_detail')
]