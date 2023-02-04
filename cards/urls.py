from django.urls import path
from .views import CardCreateView, CardListView, CardUpdateView,BoxView,CardDeleteView
urlpatterns = [
    path(
        "",
        CardListView.as_view(),
        name="card-list"
    ),
    path('new', CardCreateView.as_view(), name='card-create'),
    path('edit/<int:pk>', CardUpdateView.as_view(), name='card-update'),
    path('delete/<int:pk>', CardDeleteView.as_view(), name='card-delete'),
    path('box/<int:box_num>',BoxView.as_view(), name='box')
]
