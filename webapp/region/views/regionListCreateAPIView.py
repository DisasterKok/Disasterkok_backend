from rest_framework.generics import ListCreateAPIView

from notification.models import Notification
from region.models import Region
from region.serializers import RegionSerializer


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        notification, created = Notification.objects.get_or_create(user=user)
        serializer.save(notification=notification)
