from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from notification.models import Notification
from region.models import Region
from region.serializers import RegionSerializer


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if not queryset:
            exist = False
        else:
            exist = True

        data = {
            "exist": exist,
            "results": serializer.data,
        }

        return Response(data)

    def perform_create(self, serializer):
        user = self.request.user
        notification, created = Notification.objects.get_or_create(user=user)
        serializer.save(notification=notification)
