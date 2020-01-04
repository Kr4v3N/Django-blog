from django.shortcuts import render

from pyblog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
