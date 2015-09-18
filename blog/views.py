from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import contato
from .models import comentarios
from .models import categoria

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def categoria_list(request) :
    return render(request, 'blog/categoria_list.html',{})

def coment_list(request):
    return render(request, 'blog/coment_list.html', {})

def contato_list(resquest):
    return render(request, 'blog/contato_list', {})
