#데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer #로직 작성시 필요
# status에 따라 직접 Response를 처리할 것
from rest_framework import generics
from rest_framework import mixins


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # get은 list메소드를 내보내는 메소드    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # post는 create를 내보내는 메소드
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # DetailView의 get은 retrieve를 내보내는 메소드
    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, *kwargs)
   
    #put은 update를 내보내는 메소드
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # delete는 destroy를 내보내는 메소드
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)