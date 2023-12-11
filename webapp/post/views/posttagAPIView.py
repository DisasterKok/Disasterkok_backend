import re
from post.disasterTag import disaster_to_word_mapping
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostTagSerializer

natural_disaster = ['태풍', '호우','폭설', '지진/해일', '산사태', '우박', '낙뢰/뇌우', '황사/미세먼지','한파', '강풍', '가뭄', '산불', '폭염']
social_disaster = ['화재', '건축물붕괴','폭발', '도로교통사고', '철도/지하철 사고', '정전/전력부족', '감염병','테러사고', '인파사고']
disaster = set(natural_disaster+social_disaster)
disaster_list = natural_disaster + social_disaster

class PostTagAPIView(APIView):
    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        pattern = re.compile(r'\b(\w+)(?:을|를|이|가)\s+\w+\b')
        matches = pattern.findall(title)
        matches_set = set(matches)

        tag = []
        for element in matches_set:
            related_disasters = disaster_to_word_mapping.get(element, [])
            tag.extend(related_disasters)

        if tag:
            return Response({"tags": tag}, status=200)
        else:
            disaster_list.sort()
            return Response({"tags": disaster_list}, status=200)
