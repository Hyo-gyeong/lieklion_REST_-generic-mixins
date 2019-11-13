from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
#검색기능 갖다쓰기
from rest_framework.filters import SearchFilter
#permission
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]    
    
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    #검색
    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)


# 서로 다른 유저 둘 이상을 만들어야 그 중 한 유저를 기반으로 필터링을 할 수 있으니까#1번 유저 shin 1-4 #2번 유저 hyo 1-5 #by createsuperuser
    def get_queryset(self):
        #여기 내부에서 쿼리를 다 처리한 후 return하는것이 좋음
        qs = super().get_queryset()
        #qs = qs.filter(author__id = 2)
        #.exclude도 있음

        # 지금 로그인한 유저의 글만 필터링 해라 라는게 더 좋으니까

        # 만약 로그인이 되어있다면 -> 로그인한 유저의 글만 필터링
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        # 만약 로그인이 안되어 있다면 -> 비어있는 쿼리셋을 리턴해라
        else:
            qs = qs.none() #empty
        return qs

    # 저장할때 사용자도 저장해줘라
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)