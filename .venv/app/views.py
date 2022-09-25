from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Categories
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# *** Home request, returns all posts and renders the Index (Home) page.
def home(request):
    context = {
        'posts': Post.objects.all(),
        }
    return render(request, 'app/index.html', context)        

#------------------------------------------------
#----------------- Post Views -------------------
#------------------------------------------------
# *** PostListView used to view the list of posts within the Index (Home) page.
class PostListView(ListView):
    model = Post
    template_name = 'app/index.html'
    context_object_name = 'posts'
    #Sorting by lastest date
    ordering = ['-date_posted']
    #Showing first 5
    paginate_by = 5

    #Def used to pass through extar model data to Index, used for filtering drop down options.
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        #Code from [18] (see reference)
        context.update({
            'categories': Categories.objects.all(),
            'authors' : User.objects.values('username'),
        })
        return context

# *** Detail view for post enteries
class PostDetailView(DetailView):
    model = Post

# *** Create view used to create new Posts
#Code from tutorial - [10] (see references)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #Showing required fields to users
    fields = ['title', 'category', 'content']
    
    #Checking if form is valid first before submitting
    def form_valid(self, form):
        form.instance.author = self.request.user        
        return super().form_valid(form)

# *** Update view to update selected Post
#Code from tutorial - [10] (see references)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #Showing required fields to users
    fields = ['title', 'category', 'content']

# *** Checking if form is valid first before submitting
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        #Checking if user is the post user or the super user, to allow the user to edit the post
        if self.request.user == post.author or self.request.user.is_superuser == True:
            return True
        return False

# *** Delete view used to delete selected Post
#Code from tutorial - [10] (see references)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #Sending user back to the index page if successful 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        #Checking if user is the post user or the super user, to allow the user to delete the post
        if self.request.user == post.author or self.request.user.is_superuser == True:
            return True
        return False


#------------------------------------------------
#----------------- Filter Views -----------------
#------------------------------------------------
# *** UserPostListView used to view all the post by the user selected
class UserPostListView(ListView):
    model = Post
    #Template to use
    template_name = 'app/user_posts.html'
    context_object_name = 'posts' 
    #Showing first 5   
    paginate_by = 5

    #Checking for username passed through, if not send 404 error
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        #Show by lastest first
        return Post.objects.filter(author=user).order_by('-date_posted')

# *** CategoryPostListView used to view all the post by the user selected
class CategoryPostListView(ListView):
    model = Post
    #Template to use
    template_name = 'app/category_posts.html'
    context_object_name = 'posts'    
    #Showing first 5   
    paginate_by = 5

    #Checking for category passed through, if not send 404 error
    def get_queryset(self):
        scategory = get_object_or_404(Categories, category=self.kwargs.get('category'))
        return Post.objects.filter(category=scategory).order_by('-date_posted')


#------------------------------------------------
#-------------- Categories Views ----------------
#------------------------------------------------
# *** CategoriesListView used to view the list of categories within the Category List page.
class CategoriesListView(ListView):
    model = Categories
    template_name = 'app/category_list.html'
    context_object_name = 'categories'

# *** Create view used to create new Category
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    #Setting required fields
    fields = ['category']
    #Sending user back to categories list when finished
    success_url = '/categories/'
    
    #Checking if form is valid first before submitting
    def form_valid(self, form):  
        return super().form_valid(form)

# *** Update view to update selected Post
class CategoriesUpdateView(UpdateView):
    model = Categories
    #Setting required fields to update
    fields = ['category']
    #Sending user back to categories list when finished
    success_url = '/categories/'

    #Checking if form is valid first before submitting
    def form_valid(self, form):
        return super().form_valid(form)

#Returning true to update
    def test_func(self):        
        return True

# *** Delete view used to delete selected Category
class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Categories
    #Sending user back to the categories page if successful 
    success_url = '/categories/'    

    def test_func(self):
        #Checking if user is a super user, if not refuse user entry to url
        if self.request.user.is_superuser == True:
            return True
        return False

#------------------------------------------------
#----------------- About View -------------------
#------------------------------------------------
# *** Def to show About page when requested
def about(request):
    return render(request, 'app/about.html', {'title': 'About'})
