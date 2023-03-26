from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from TemitopePortfolioApp.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'photo')


class CatAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CatSerializer

    def get_object(self):
        return Cat.objects.first()