from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault


from .models import Post
from comment.api.models import Comment
from custom_user.serializer import LikeUserSerializer


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['content', 'mode']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class UpDelPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['content', 'mode',]


class DetailPostSerializer(serializers.ModelSerializer):
    count_like = serializers.SerializerMethodField()
    count_comment = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_count_like(self, obj: Post):
        return obj.like.all().count()

    def get_count_comment(self, obj: Post):
        return obj.comment_of_post.all().count()
    
    def get_is_liked(self, obj: Post):
        user = self.context['request'].user
        if user in obj.like.all():
            return True
        else:
            return False

    class Meta:
        model = Post
        fields = ['content', 'user', 'like', 'count_like', 'count_comment', 'is_liked']
    

class LikeSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    like = LikeUserSerializer(many=True, read_only=True)

    def check_user_is_like(self, post : Post, user):
        if user in post.like.all():
            return True
        else:
            return False

    def create(self, validated_data):
        post = self.get_post()
        user = validated_data['user']
        is_liked = self.check_user_is_like(post, user)
        if not is_liked:
            post.like.add(user)
        return post

    def get_post(self) -> Post:
        id = self.context['view'].kwargs['post_id']
        post = Post.objects.get(id=id)
        return post
    
    def remove_user(self, validated_data):
        post = self.get_post()
        user = validated_data['user']
        is_liked = self.check_user_is_like(post)
        if is_liked:
            post.like.remove(user)
    
    
        
