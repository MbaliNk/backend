from calendar import c
from cgitb import html
from multiprocessing import context
from operator import index
from re import template
from telnetlib import STATUS
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Book, Post, Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import Commentforms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def displayTime(request):
    now = datetime.datetime.now()
    html = "Time is{}".format(now)
    return HttpResponse(html)

def greeting(request):
    return HttpResponse("Welcome to Gossip girl world")

# class based view
class Myview(TemplateView):
    
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        template_name = "index.html"
        context = {
            "page": template_name
        }
        return context
        # return HttpResponse("template_name")


     # book_list
def book_list(request):
     books = Book.objects.all()
     return render(request, "book_list.html", {"books": books})



# view for all posts
def Post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try: 
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'page':page,'posts':posts})

# views for all posts and post_list
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post , status ='published', publish__year=year,publish__month=month,publish__day=day )
    comments = post.comments.filter(active = True)
    new_comment = None
    if request.method =='POST':
        comment_form = Commentforms(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
         comment_form =Commentforms()        
    return render(request,'post_detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})

# Create your views here.
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in {username}.")
                return redirect("blog:profile")
            else:
             messages.error(request, F"Invalid username or password")
        else:
         messages.error(request, F"Invalid username or password")
    form = AuthenticationForm()            
    return render(request,"authenticate/login.html", context={"form":form})

@login_required(login_url='blog:login')
def profileView(request):
    return render(request, 'profile.html',{})

def logout_view(request):
    logout(request)
    return redirect('/')

def aboutpage(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

