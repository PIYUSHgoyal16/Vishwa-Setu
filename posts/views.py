"""Posts Views"""

# Django
import numpy as np
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm2,PostForm
from .textToImageAPI.textToImage import textToImage
from datetime import datetime
# from django.http import HttpResponse

# Models
from posts.models import Post
from users.models import Profile

def CreatePostView(request):
    if request.method=="POST":
        form = PostForm2(request.POST)
        if form.is_valid():
            profilePK = str(request.user.profile.pk)
            literature = form.cleaned_data['literature']

            textToImage([literature],profilePK)
            ProfileObj = Profile.objects.get(pk=int(profilePK))
            dateNow = datetime.now()
            PostObj = Post(profile=ProfileObj, title="Literature Post", photo="posts/photos/"+str(dateNow)+"_"+profilePK+".png")
            PostObj.save()
            return render(request, "posts/feed.html",{})
    form = PostForm2()
    return render(request, "posts/new.html", {'form':form})


class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Detail view posts"""
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
