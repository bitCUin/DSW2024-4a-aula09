from django.shortcuts import render, redirect

from instacaio.forms import PostForm
from instacaio.models import Post


def inicio(request):
    posts = Post.objects.all()
    return render(request, 'inicio.html', {
        'posts': posts
    })

# Create your views here.
def criar_post(request):
    if (request.method == "POST"):
        formulario = PostForm(request.POST, request.FILES)
        if (formulario.is_valid):
            formulario.save()
            return redirect("inicio")
    else:
        formulario = PostForm()
    return render(request, 'postar.html', {
        "formulario": formulario
    })