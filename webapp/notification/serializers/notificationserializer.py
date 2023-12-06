from rest_framework import serializer

from notification.models import Notification


class NotificationSerializer(serializer.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('__all__')