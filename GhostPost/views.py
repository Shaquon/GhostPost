from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from GhostPost.models import Post
from GhostPost.forms import add_post_form
from django.contrib import messages
from django.utils.timezone import now


def index_view(request):
    html = "index.html"

    posts = Post.objects.all()[::-1]

    return render(request, html, {"posts": posts})


def handle_upvote_view(request):
    if request.method == "POST":
        id = request.POST.get("id")
        post = Post.objects.filter(id=id).first()
        post.upvotes += 1
        post.save()
        return redirect("/")


def handle_downvote_view(request):
    if request.method == "POST":
        id = request.POST.get("id")
        post = Post.objects.filter(id=id).first()
        post.downvotes += 1
        post.save()
        return redirect("/")


def add_post_view(request):
    html = 'add_post.html'

    if request.method == "POST":
        form = add_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data['is_boast'],
                content=data['content'],
                upvotes=0,
                downvotes=0,
                submit_time=now()
            )
            messages.add_message(request, messages.INFO)

        return HttpResponseRedirect(reverse('homepage'))

    form = add_post_form()
    return render(request, html, {'form': form})


def sorter(posts):
    posts.upvotes - posts.downvotes


def top_votes_view(request):
    html = "index.html"

    posts = sorted(
        Post.objects.all(),
        key=sorter,
        reverse=True
    )

    return render(request, html, {"posts": posts})


def boasts_time_view(request):
    html = 'index.html'

    posts = Post.objects.filter(is_boast=True)

    return render(request, html, {
        'posts': posts,
        'votes': '/boasts/votes/',
        'time': '/boasts/'})


def roasts_time_view(request):
    html = 'index.html'
    posts = Post.objects.filter(is_boast=False)[::-1]

    return render(request, html, {
        'posts': posts,
        'votes': '/roasts/votes/',
        'time': '/roasts/'
    })


def boast_votes_view(request):
    html = 'index.html'

    boasts = Post.objects.sorted(
        Post.objects.filter(is_boast=True),
        key=sorter,
        reverse=True
        )
    return render(
        request,
        html,
        {'posts': posts,
         'votes': '/boasts/votes',
         'time': '/boasts'
         })


def roast_votes_view(request):
    html = 'index.html'

    posts = Post.objects.sorted(
        Post.objects.filter(is_boast=False),
        key=sorter,
        reverse=True
        )
    return render(
        request,
        html,
        {'posts': posts,
         'votes': '/roasts/votes',
         'time': '/roasts'
         })
