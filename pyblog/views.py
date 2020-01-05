from django.shortcuts import render

from pyblog.models import Post
from pyblog import model_helpers
from pyblog import navigation


# Create your views here.
def post_list(request, category_name=model_helpers.post_category_all.slug()):
    category, posts = model_helpers.getCategory_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'category': category,
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/post_list.html', context)
