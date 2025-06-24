from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CategoryPostListView, TagPostListView, AuthorPostListView
)
from .views.comment import CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('category/<slug:slug>/', CategoryPostListView.as_view(), name='posts_by_category'),
    path('tag/<slug:slug>/', TagPostListView.as_view(), name='posts_by_tag'),
    path('author/<str:username>/', AuthorPostListView.as_view(), name='posts_by_author'),

    path('post/<slug:slug>/comment/', CommentCreateView, name='add_comment'),
]