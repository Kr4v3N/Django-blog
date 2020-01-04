from django.shortcuts import render

from pyblog.models import Post
from pyblog import model_helpers


# Create your views here.
def post_list(request, category_name=model_helpers.post_category_all.slug()):
    category, posts = model_helpers.getCategory_and_posts(category_name)

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
