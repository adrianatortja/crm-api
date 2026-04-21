from django.urls import path
from .views import InteractionListCreateView, InteractionDetailView

urlpatterns = [
    path("", InteractionListCreateView.as_view(), name="interaction-list-create"),
    path("<int:pk>/", InteractionDetailView.as_view(), name="interaction-detail"),
]
