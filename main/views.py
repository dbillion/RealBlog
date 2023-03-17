from django.shortcuts import render
# from django_filters import  ProductFilter
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post, ProductFilter,Owner


def index(request):
    postlist = Post.objects.all()
    context = {'postlist': postlist}
    return render(request, 'main/index.html', context)


def about(request):
    postlist = Owner.objects.all()
    context = {'postlist': postlist}
    return render(request, 'main/about.html', context)


def blog(request):
    q = request.GET.get("q", None)
    if q is None or q is "":
        postlist = Post.objects.all()
    elif q is not None:
        postlist = Post.objects.filter(postname__contains=q)
    context = {'postlist': postlist}
    return render(request, "main/blog.html", context)


def postdetails(request, pk):
    postlist = get_object_or_404(Post, pk=pk)
    poster = Post.objects.all()
    context = {'postlist': postlist, 'poster': poster}
    return render(request, "main/postdetails.html", context)


def product_filter(request):
    filter = ProductFilter(request.GET, queryset=Post.objects.all())
    return {'filter': filter}
