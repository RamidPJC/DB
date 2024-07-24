from http.client import HTTPResponse

from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
def index(request):
    s_value = request.GET.get('_search', '')

    if s_value:
        posts = Post.objects.filter(title__icontains=s_value)
        if posts.count() == 0:
            return redirect('home')
    else:
        posts = Post.objects.all()

    cats = Cate.objects.all()
    user = request.user
    paginator = Paginator(posts, 10)
    num_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(num_page)
    for i in page_obj.object_list:
        if len(i.cont) > 30:
            i.cont = i.cont[:30] + '...'
        i.category_names = ', '.join([j.title for j in i.category.all()])

    context = {
        'posts': posts,
        'cats': cats,
        'user': user,
        'page_obj': page_obj,
        'search_value': s_value,
    }
    return render(request, 'index.html', context)


def post(request, pk):
    cats = Cate.objects.all()
    post = Post.objects.get(pk=pk)
    post.category_names = ', '.join([j.title for j in post.category.all()])
    comments = Comments.objects.filter(post=post)
    user = request.user
    Post.objects.filter(pk=pk).update(views=models.F('views') + 1)
    form = AddComment()
    form2 = RatePostForm()
    rat = RatePost.objects.filter(post=post)
    middle_rate = 0
    if rat.exists():
        middle_rate += sum([i.rate for i in rat]) / rat.count()
    else:
        middle_rate = 0
    prof_user = Profile.objects.get(name=user)

    if request.method == "POST":
        if '_comm' in request.POST:
            form = AddComment(request.POST)
            if form.is_valid():
                comm = form.save(commit=False)
                comm.author = request.user
                comm.post = post
                comm.save()
                return redirect('post', pk=pk)
        elif '_rate' in request.POST:
            form2 = RatePostForm(request.POST)
            if form2.is_valid():
                rate_value = form2.cleaned_data['rate']
                existing_rate = RatePost.objects.filter(post=post, person=prof_user).first()

                if existing_rate:
                    existing_rate.rate = rate_value
                    existing_rate.save()
                else:
                    new_rate = form2.save(commit=False)
                    new_rate.post = post
                    new_rate.person = prof_user
                    new_rate.save()

                return redirect('post', pk=pk)

    return render(request, 'post.html', {
        'post': post,
        'cats': cats,
        'comments': comments,
        'form': form,
        'user': user,
        'form2': form2,
        'middle_rate': str(middle_rate)[:3]
    })


def detail_cat(request, pk):
    cat = Cate.objects.get(pk=pk)
    s_value = request.GET.get('_search', '')

    if s_value:
        posts = Post.objects.filter(title__icontains=s_value)
        if posts.count() == 0:
            return redirect('home')
    else:
        posts = Post.objects.filter(category=cat)
    cats = Cate.objects.all()
    paginator = Paginator(posts, 10)
    num_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(num_page)
    for i in page_obj.object_list:
        if len(i.cont) > 30:
            i.cont = i.cont[:30] + '...'
        i.category_names = ', '.join([j.title for j in i.category.all()])
    return render(request, 'category.html', {"posts": posts, "cat": cat, "cats": cats, "page_obj": page_obj})

def side(request):
    cats = Cate.objects.all()
    return render(request, '_side.html', {'cats': cats})

def add_post(request):
    if request.method == "POST":
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewPost()
    return render(request, 'add_post.html', {'form': form})

def anim(request):
    return render(request, 'anim.html')

def chat_view(request):
    if request.method == 'POST':
        form = Mess(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('chat_view')
    else:
        form = Mess()
        message = Messenger.objects.all()[:30]
        return render(request, 'chat.html', {'form': form, 'message': message})

def get_profile(request, username):
    user = User.objects.get(username=username)
    prof = Profile.objects.get(name=user)
    now_user = request.user
    if request.user.username == prof.name.username:
        if request.method == 'POST':
            form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('get_profile', user.username)
        else:
            form = EditProfile(instance=request.user.profile)
        return render(request, 'profile.html', {'prof': prof, 'form': form, 'now_user': now_user})
    else:
        return render(request, 'profile.html', {'prof': prof, 'now_user': now_user})

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(name=request.user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})

def log(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logou(request):
    logout(request)
    return redirect('home')

def edit_pic(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_profile')
    else:
        form = EditProfile()
    return render(request, 'profile.html', {"form": form})

def predl(request):
    posts = Predlozka.objects.all()
    cats = Cate.objects.all()
    user = request.user
    paginator = Paginator(posts, 10)
    num_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(num_page)
    for i in page_obj.object_list:
        if len(i.cont) > 30:
            i.cont = i.cont[:30] + '...'
        i.category_names = ', '.join([j.title for j in i.category.all()])
    return render(request, 'predl.html', {'posts': posts, 'cats': cats, 'user': user, 'page_obj': page_obj})

def copy_to_posts(request):
    predl = Predlozka.objects.all()
    if request.method == "POST":
        for i in predl:
            Post.objects.create(title=i.title, category=i.category, content=i.content, photo=i.photo)

def predl_detail(request, pk):
    cats = Cate.objects.all()
    post = get_object_or_404(Predlozka, pk=pk)
    post.category_names = ', '.join([j.title for j in post.category.all()])
    if request.method == "POST":
        new_post = Post.objects.create(
            title=post.title,
            cont=post.cont,
            photo=post.photo
        )
        new_post.category.set(post.category.all())
        new_post.save()
        post.delete()
        return redirect('predl')
    if request.method == "POST" and request.POST.get('_method'):
        post.delete()
    return render(request, 'predl_detail.html', {'post': post, 'cats': cats, 'user': request.user})

def update_post_from_predl(request, pk):
    post = Predlozka.objects.get(pk=pk)
    if request.method == "POST":
        form = NewPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('predl_detail', pk)
    else:
        form = NewPost(instance=post)
    return render(request, 'update_post_from_predl.html', {'form': form})

def add_post_admin(request):
    if request.method == "POST":
        form = NewPostAdmin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewPostAdmin()
    return render(request, 'add_post_admin.html', {'form': form})






