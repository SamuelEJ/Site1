from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import MonthArchiveView
from . import functionss
#import django.templatetags


#Make a model available to the views
from .models import Post, PostView

def index(request):
    return HttpResponse("Hello, world. You're at the Blog_App index.")

def blogHome(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)  # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_posts = paginator.page(paginator.num_pages)

    return render(request, 'BlogHome.html', {'blog_posts': blog_posts})







def blogSearchList(request, text_name=None, yearParameter = 1, monthParameter = 1):
    try:
        if 'q' in request.GET and request.GET['q']:
         text_name = request.GET['q']
        posts = Post.objects.filter(Title__icontains=text_name)
        return render(request, 'BlogSearch.html',
                      {'posts': posts, 'query': text_name})
    except:pass

    try:
        posts = Post.objects.filter(Title__icontains=text_name)
        return render(request, 'BlogSearch.html',
                      {'posts': posts, 'query': text_name})
    except: pass

    try:
       posts = Post.objects.filter(year=yearParameter).filter(monthNumber=monthParameter)
       return render(request, 'BlogSearch.html',
                      {'posts': posts, 'query': yearParameter, 'query':monthParameter})
    except:pass


    raise Http404("Submit search term")

    #blog_posts = Post.objects.all()

    #return render(request, 'BlogSearch.html', {'PostsList': blog_posts})


def BlogPostDetail(request, id):
    try:
        PostDetail = Post.objects.prefetch_related('Tags').get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'BlogPostdetail.html', {'Post': PostDetail})


def BlogPostViewDetail(request, id):
    try:
        PostViewDetail = PostView.objects.get(pk=id)
    except PostView.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'BlogPostViewDetail.html', {'Post': PostViewDetail})


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "createdDate"
    allow_future = True



def ArchiveView(request):
    from django.db import connection, transaction
    cursor = connection.cursor()
# Data retrieval operation

    #cursor.execute("SELECT * FROM mysite_blog_app_db.post_archive_view")
    cursor.execute("SELECT * FROM mysite_blog_app_db.post_archive_view;")
    archives = functionss.dictfetchall(cursor)

    return render(request, 'sub_archive_pane.html', {"archives":archives})






