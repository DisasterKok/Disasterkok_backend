from rest_framework.response import Response
from rest_framework.views import APIView
from region.models import Region

class RegionOnOffAPIView(APIView):
    lookup_url_kwarg = 'region_id'

    def post(self, request, *args, **kwargs):
        region_id = self.kwargs.get(self.lookup_url_kwarg)
        region = Region.objects.get(id=region_id)
        if region.onOff == False:
            region.onOff = True
            region.save()
        else:
            region.onOff = False
            region.save()
        return Response({'message': '변경되었습니다.'}, status=200)