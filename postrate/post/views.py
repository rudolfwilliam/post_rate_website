from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-pub_date')
    template = loader.get_template('post/index.html')
    context = {'post_list': post_list, }

    if request.method == "POST":
        like = request.POST.get('like')
        dislike = request.POST.get('dislike')
        if like:
            post = Post.objects.get(id=like)
            post.likes = (post.likes + 1)
            post.save()
        elif dislike:
            post = Post.objects.get(id=dislike)
            post.dislikes = (post.dislikes + 1)
            post.save()

        return HttpResponse(template.render(context, request))

    else:

        return HttpResponse(template.render(context, request))


def create(request):
    template = 'post/create.html'
    if request.method == 'POST':
        post = Post()
        post.post_text = request.POST.get("post_text")
        post.pub_date = timezone.now()
        post.save()

        return render(request, template)

    else:

        return render(request, template)
