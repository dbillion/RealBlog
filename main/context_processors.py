from .models import Post, ProductFilter


def product_filter(request):
    filters = ProductFilter(request.GET, queryset=Post.objects.all())
    return {'filters': filters}
