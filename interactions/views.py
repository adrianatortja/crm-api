from rest_framework import generics, permissions
from .models import Interaction
from .serializers import InteractionSerializer


class InteractionListCreateView(generics.ListCreateAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(
            lead__client__user=self.request.user
        ).order_by("-created_at")


class InteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(
            lead__client__user=self.request.user
        )
        