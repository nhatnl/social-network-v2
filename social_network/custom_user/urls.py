from django.urls import path

from .views import CurrentUserDetail, DetailUser, ListUser

urlpatterns = [
    path('', ListUser.as_view(), name='list_user'),
    path('me/', CurrentUserDetail.as_view(), name='current_user_detail'),
    path('<int:user_id>/', DetailUser.as_view(), name='detail_user'),

]