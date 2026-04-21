from rest_framework import serializers
from .models import Lead
from clients.models import Client


class LeadSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.name')

    class Meta:
        model = Lead
        fields = [
            'id',
            'client',
            'client_name',
            'title',
            'source',
            'status',
            'notes',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'client_name']

    def validate_client(self, value):
        request = self.context['request']
        if value.user != request.user:
            raise serializers.ValidationError(
                "You can only create leads for your own clients."
            )
        return value
    