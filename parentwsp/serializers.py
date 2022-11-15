from rest_framework.serializers import ModelSerializer

from .models import Notification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "id",
            "session",
            "message",
            "chat_name",
            "sender",
            "sender_number",
        )
