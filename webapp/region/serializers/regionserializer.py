from rest_framework import serializers

from region.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'default',
            'onOff',
            'name',
            'address',
            'roadAdress',
            'zoneCode',
            'xCoordinate',
            'yCoordinate',
            'aliasType',
        )

