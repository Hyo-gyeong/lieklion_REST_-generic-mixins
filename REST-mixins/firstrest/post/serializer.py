from .models import Post # 모델을 기반으로 직렬화시킬것이기 때문에
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ('id', 'title', 'body')
        #read_only_fields = ('title',)
        #write_only_fields = ('title',)