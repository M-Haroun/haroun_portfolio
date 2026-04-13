from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post,Comment
from .forms import CommentForm, PostForm

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(published=True)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        # Accepted comments only
        context['comments'] = self.object.comments.filter(is_approved=True)
        return context
    
    def post(self, request, *args, **kwargs):
        # redirect not login user to login page
        if not request.user.is_authenticated:
            return redirect('login') 
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()  # is_approved = False 
        return redirect(self.request.path)

    
# Reusable Mixin for Superuser Only
class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# Create (Admin & staff)
class BlogCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')
    
    # don't show slug field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('slug', None)
        return form

# Update (Admin & staff)
class BlogUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog:list')
    
    # don't show slug field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('slug', None)
        return form


# Delete (Admin & staff)
class BlogDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog:list')
