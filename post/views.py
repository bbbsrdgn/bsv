from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment, User 
from .forms import PostForm, CommentForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



def anasayfa(request):
	posts = Post.objects.all()
	return render(request, 'anasayfa.html', {'posts': posts})

def tum_sorular(request):
	posts = Post.objects.all()
	return render(request, 'tum_sorular.html', {'posts': posts})

def cevapsizlar(request):
    posts = Post.objects.all()
    return render(request, 'cevapsizlar.html', {'posts':posts})

def en_yeniler(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'en_yeniler.html', {'posts': posts})

def soru_sor(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.pub_date = timezone.now()
            post.save()
            pk = post.pk
            return redirect('detail', pk=pk)
    else:
        form = PostForm()
    return render(request, 'soru_sor.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post': post})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)



def kayit(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'kayit.html', {'form': form})

def iletisim(request):
    post = get_object_or_404(User)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages = form.save(commit=False)
            messages.post = post
            messages.save()
            return redirect('post_detail')
    else:
        form = CommentForm()
    return render(request, 'iletisim.html', {'form': form})


