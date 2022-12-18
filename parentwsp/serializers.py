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
            "date",
            "sender",
            "sender_number",
            "sender_name",
        )
