from django.urls import path
from .views import SnacksListView, SnacksDetailView, SnacksCreateView, SnacksUpdateView, SnacksDeleteView
urlpatterns = [
    path('',SnacksListView.as_view(),name='snack_list'),
    path('<int:pk>/',SnacksDetailView.as_view(),name='snack_detail'),
    path('create/',SnacksCreateView.as_view(),name='snack_create'),
    path('update/<int:pk>',SnacksUpdateView.as_view(),name='snack_update'),
    path('delete/<int:pk>',SnacksDeleteView.as_view(),name='snack_delete')
]