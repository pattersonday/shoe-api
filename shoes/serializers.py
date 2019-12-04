from rest_framework.serializers import HyperlinkedModelSerializer

from shoes import models


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer

        fields = ['name', 'website']


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType

        fields = ['style']


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor

        fields = ['color_name']


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Shoe

        fields = ['size', 'brand_name', 'manufacturer', 'color', 'material', 'shoe_type', 'fasten_type']