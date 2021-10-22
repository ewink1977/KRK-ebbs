from rest_framework.response import Response
from .models import Post, PostReply
from rest_framework import generics, viewsets, permissions
from .serializers import PostSerializer, PostReplySerializer, AddPostSerializer

# POST VIEWSET
class AllPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_reply=False).order_by('created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer


class AllReplyViewSet(viewsets.ModelViewSet):
    queryset = PostReply.objects.filter(is_reply=True).order_by('created_at')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostReplySerializer


class SinglePostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, pk):
        single_post = Post.objects.get(pk=pk)
        serializer = PostSerializer(single_post)
        return Response(serializer.data)

    def delete(self, request, pk):
        single_post = Post.objects.get(pk=pk)
        single_post.destroy()
        return Response
