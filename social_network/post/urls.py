from django.conf.urls import include
from django.urls import path

from .api.views import CreatePost, PostViewSet, LikeViewSet

urlpatterns = [
    path('', PostViewSet.as_view({
                                    'get':'list',
                                    }), name='list_post'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('<int:post_id>/', PostViewSet.as_view({
                                            'get':'retrieve', 
                                            'put':'update',
                                            'patch':'update',
                                            'delete': 'destroy',
                                            }), name='viewset_post'),
    path('<int:post_id>/like/', LikeViewSet.as_view({
                                            'post': 'create',
                                            'get':'list',
                                            'delete':'destroy'
    })),
    path('<int:post_id>/comment/', include('comment.urls'))

]