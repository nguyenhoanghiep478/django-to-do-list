from django.views.generic import ListView
from ..models import Category,Tag
from django.shortcuts import get_object_or_404
class CategoryPostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.post_set.filter(is_published=True).order_by('-created_at')

class TagPostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return tag.post_set.filter(is_published=True).order_by('-created_at')