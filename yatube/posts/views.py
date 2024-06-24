from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post, Group
from .forms import TextForm

def index(request):
    title = 'Yatube'
    template = 'posts/index.html'
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[::-1][:10]

    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

def group(request, slug):
    template = 'posts/group.html'
    group = get_object_or_404(Group, slug=slug)

    context = {
        'title': group.title,
        'group': group,
        'posts': group.posts.filter(pub_date__lte=timezone.now()).order_by('pub_date')[::-1],
        'posts_count': len(group.posts.all())
    }
    return render(request, template, context)

@login_required
def create(request, slug):
    template = 'posts/create.html'
    group = get_object_or_404(Group, slug=slug)

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Post.objects.create(text=text, author=request.user, group=group)
            return redirect('posts:group', slug)
    else:
        form = TextForm()

    context = {
        'title': group.title,
        'group': group,
        'form': form
    }
    return render(request, template, context)