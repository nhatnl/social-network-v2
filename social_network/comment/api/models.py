
from django.db import models

from custom_user.models import CustomUser
from post.api.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='comment_of_post')
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='parent_of_comment')
    content = models.CharField(max_length=150, null=False, blank=False)
    level = models.IntegerField(
        verbose_name='comment_level', null=False, blank=False)
