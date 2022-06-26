from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView



# Create your views here.
def PostListView(request):
    model = Post
    template_name = 'blog/post_list.html'
    context = {
      'object_list': Post.objects.all()
    }
    return ListView(model, template_name, context)
    # return render(request, template_name, context)

def PostCreateView(request):
    model = Post
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:all')
    return CreateView(model, template_name, form_class, success_url)

def PostDetailView(request, slug):
    model = Post
    template_name = 'blog/post_detail.html'
    context = {
      'object': Post.objects.get(slug=slug)
    }
    return DetailView(model, template_name, context)
    # return render(request, template_name, context)

def PostUpdateView(request, slug):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:all')
    return UpdateView(model, template_name, form_class, success_url)

def PostDeleteView(request, slug):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:all')
    context = {
      'object': Post.objects.get(slug=slug)
    }
    return DeleteView(model, template_name, context, success_url)






# def PostListView(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/post_list.html', context)

# def PostCreateView(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/post_create.html', context)

# def PostDetailView(request, slug):
#     post = Post.objects.get(slug=slug)
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/post_detail.html', context)

# def PostUpdateView(request, slug):
#     post = Post.objects.get(slug=slug)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', slug=slug)
#     else:
#         form = PostForm(instance=post)
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/post_update.html', context)

# def PostDeleteView(request, slug):
#     post = Post.objects.get(slug=slug)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/post_delete.html', context)

    

