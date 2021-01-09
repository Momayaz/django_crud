from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Post
# # Create your views here.

class BlogListView(ListView):
    template_name = 'posts-list.html'
    model = Post


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields= ['title', 'author', 'body']

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields= ['title', 'author', 'body']


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('posts')