from django.urls import reverse_lazy
from django.views.generic.edit import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import render

from I4G025038MTP.blog.models import Post

# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields ="__all__"  
    success_url = ("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields ="__all__"  
    success_url = ("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields ="__all__"  
    success_url = ("blog:all")