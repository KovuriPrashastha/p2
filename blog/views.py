from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#initially
posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 7, 2020'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 8, 2020'
    }
]

# Create your views here.
#Sysntax of render function
#render(request, template_name, context=None, content_type=None, status=None, using=None)
def home(request):
    context = {
        #'posts' : posts  used the dummy data before creay=ting the class
        'posts' : Post.objects.all()#these are the obejects which we have created using the shell
    }
    return render(request, 'blog/home.html', context)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name='posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
  

#blog -> templates -> blog -> templates.html
