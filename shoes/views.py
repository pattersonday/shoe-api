from rest_framework import viewsets
from shoes import models, serializers


class ManufacturerView(viewsets.ModelViewSet):

    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class ShoeTypeView(viewsets.ModelViewSet):

    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer


class ShoeColorView(viewsets.ModelViewSet):

    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer


class ShoeView(viewsets.ModelViewSet):

    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer
