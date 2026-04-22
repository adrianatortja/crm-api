from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Lead
from .serializers import LeadSerializer


class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "source", "client"]
    search_fields = ["title", "notes", "client__name"]
    ordering_fields = ["title", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Lead.objects.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.filter(client__user=self.request.user)
    