from django.shortcuts import redirect, get_object_or_404
from ..models import Post
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required
def CommentCreateView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    return redirect('post_detail', slug=slug)