from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html',  {'posts': posts})
