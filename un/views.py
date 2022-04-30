from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class ScrollView(viewsets.ModelViewSet):
    queryset = Scroll.objects.all()
    serializer_class = ScrollSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = ProductSerializer


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializers


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = BlogPicture.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, *args, **kwargs):
        id = kwargs['pk']
        images = []
        blogs = self.queryset.filter(blog_id=id)
        serializer = self.get_serializer(blogs)
        for blog in blogs:
            picture = {
                "id": blog.id,
                'Blog': blog.blog.id,
                'image': blog.ImageURL,
            }
            images.append(picture)
        return Response({"Images": images})