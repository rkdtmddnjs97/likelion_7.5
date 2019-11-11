from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog , pk=blog_id)
    return render(request,'detail.html', {'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/app_blog/'+str(new_blog.id))

def edit(request,blog_id):
    edit_blog = Blog.objects.get(id=blog_id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request, blog_id):
    update_blog = Blog.objects.get (id = blog_id)
    update_blog.title = request.POST['title']
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('home')

def delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect('home')