from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "lead", "due_date"]
    search_fields = ["title", "description", "lead__title"]
    ordering_fields = ["due_date", "created_at", "title"]
    ordering = ["due_date", "-created_at"]

    def get_queryset(self):
        return Task.objects.filter(
            lead__client__user=self.request.user
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            lead__client__user=self.request.user
        )
        