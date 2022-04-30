from rest_framework import serializers
from .models import *


class ScrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scroll
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class FAQSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPicture
        fields = '__all__'

