from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.
#a function (def) called post_list that takes request 
#and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
#To create a new Post form, we need to call PostForm() and pass it to the template.
def post_new(request):
	#separate situations
	#first time blank
	#when we go back to the view with all form data we just typed
    if request.method == "POST":
        form = PostForm(request.POST)
        #check if form is correct
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #post_detail is the name of the view we want to go to.
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #extra pk parameter from urls. 
            #get the Post model want to edit with get_object_or_404(Post, pk=pk) 
            #and then, create a form, pass this post as an instance, 
            return redirect('post_detail', pk=post.pk)
    else:
    	#just opened a form with this post to edit
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})