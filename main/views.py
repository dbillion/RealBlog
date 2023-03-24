# from django_filters import  ProductFilter

import openai
import os
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)


# Create your views here.

from .models import Post, ProductFilter, Owner

def chatton(request):
    chatton_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        users_input = request.POST.get('users_input')
        print(users_input)
        # prompt = user_input
        # prompt = f"translate this text to chinese"
        prompt = f"if the question is related to weather- answer it: {users_input},else say: cant answer this"

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            # stop="."
            temperature=0.5
        )
        print(response)
        chatton_response = response["choices"][0]["text"]
    return render(request, 'main/blog.html', {"response": chatton_response})

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
    if q is None or q == "":
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



