from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('author', )
        extra_kwargs = {
            'image': {"required": True},
            'category': {"required": True},
        }
