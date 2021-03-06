from django.urls import path

from wykop.posts.views import (PostCreate, PostDelete, PostDetail, PostList,
                               PostUpdate)

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('new', PostCreate.as_view(), name='create'),
    path('<int:pk>', PostDetail.as_view(), name='detail'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='delete'),
]
