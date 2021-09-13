from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, ModelField


from comment.api.models import Comment
from post.api.models import Post


class CurrentPost:
    requires_context = True

    def __call__(self, serializer_field):
        post_id = serializer_field.context['view'].kwargs['post_id']
        post = Post.objects.filter(id=post_id)
        if post.exists():
            return post.first()
        else:
            return None

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CommentSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    content = serializers.CharField(max_length=150, required=True)
    post = serializers.HiddenField(default=CurrentPost())
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.filter(level=1), allow_null=True)
    level = serializers.HiddenField(default=1)

    def validate_parent(self, parent):
        if parent is not None:
            post_id = self.context['view'].kwargs['post_id']
            post = Post.objects.get(id=post_id)
            if parent.post == post:
                return parent
            else:
                raise serializers.ValidationError(
                    _('Parent Validation Error: Comment not in current Post'))
        return parent

    def set_level(self, validated_data):
        parent = validated_data.get('parent', None)
        if parent is not None:
            return 2
        else:
            return 1

    def create(self, validated_data):
        validated_data['level'] = self.set_level(validated_data)
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.parent = validated_data['parent']
        instance.level = self.set_level(validated_data)
        instance.save()
        return instance



