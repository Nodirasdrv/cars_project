from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'child': {'required': True}}

    def to_representation(self, instance):
        representation = super(CategorySerializer, self).to_representation(instance)
        if instance.children.exists():
            representation['child'] = CategorySerializer(instance.children.all(),
                                                         many=True).data
        return representation

