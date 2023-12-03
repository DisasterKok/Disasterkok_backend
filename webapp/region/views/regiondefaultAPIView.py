from rest_framework.response import Response
from rest_framework.views import APIView

from notification.models import Notification
from region.models import Region


class RegionDefaultAPIView(APIView):
    lookup_url_kwarg = 'region_id'

    def post(self, request, *args, **kwargs):
        region_id = self.kwargs.get(self.lookup_url_kwarg)
        user = request.user
        notification = Notification.objects.get(user=user)
        regions = Region.objects.filter(notification=notification)
        for region in regions:
            region.default = False
            region.save()

        default_region = Region.objects.get(id=region_id)
        default_region.default = True
        default_region.save()

        return Response({'message': '변경되었습니다.'}, status=200)