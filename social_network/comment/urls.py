from django.urls import path

from .api.views import CreateComment, UpDelComment, ListComment, ListSubComment

urlpatterns = [
    path('', ListComment.as_view(), name='comment_list'),
    path('create/', CreateComment.as_view(), name='comment_create'),
    path('<int:comment_id>/', UpDelComment.as_view(), name='comment_update_delete'),
    path('<int:comment_id>/sub/', ListSubComment.as_view(), name='sub_comment_list'),
]