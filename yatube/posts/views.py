from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Post, Group


def index(request):
    title = 'Последние обновления на сайте'
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = get_object_or_404(Group, slug=slug)
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
