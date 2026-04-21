from rest_framework import serializers
from .models import Interaction


class InteractionSerializer(serializers.ModelSerializer):
    lead_title = serializers.CharField(source="lead.title", read_only=True)

    class Meta:
        model = Interaction
        fields = [
            "id",
            "lead",
            "lead_title",
            "interaction_type",
            "subject",
            "notes",
            "created_at",
        ]
        read_only_fields = ["id", "lead_title", "created_at"]

    def validate_lead(self, value):
        request = self.context["request"]

        if value.client.user != request.user:
            raise serializers.ValidationError(
                "You can only add interactions to your own leads."
            )

        return value
    
    