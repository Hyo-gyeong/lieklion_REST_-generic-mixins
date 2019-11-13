from post.models import Post
from post.serializer import PostSerializer #로직 작성시 필요

from rest_framework import viewsets

#pagination 파이썬 파일로 따로 만들어 import해도 됨.
from rest_framework.pagination import PageNumberPagination
# @action처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse 

# ModelViewSet은 ListView와 DetailView에 대한 CRUD가 모두 가능

#페이지 네이션
class MyPagination(PageNumberPagination):
    #pass or
    PAGE_SIZE =  5

class PostViewSet(viewsets.ReadOnlyModelViewSet):
# 페이지네이션을 할 때에는 반드시 레코드를 정렬한 상태에서 페이지네이션을 수행할 것
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
# cusomized pagination - 골라서 페이지네이션하기
    pagination_class = MyPagination #import필요

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    #POST방식을 원하면 @action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #그냥 글자'하하호호'를 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("하하호호")