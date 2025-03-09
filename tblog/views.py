from django.shortcuts import render
from .models import Post



def blog_home(request):
    return render(request, 'blog_home.html')


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts_list.html', {'posts' : posts, 'Post': Post})
