from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Interaction
from .serializers import InteractionSerializer


class InteractionListCreateView(generics.ListCreateAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["interaction_type", "lead"]
    search_fields = ["subject", "notes", "lead__title"]
    ordering_fields = ["created_at", "subject"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Interaction.objects.filter(
            lead__client__user=self.request.user
        )


class InteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(
            lead__client__user=self.request.user
        )
        