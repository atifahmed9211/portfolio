from django.shortcuts import render, get_object_or_404
from .models import blog

def allblogs(request):
    blogs=blog.objects
    return render(request,'blog/allblog.html',{'blogs':blogs})
def detail(request,blog_id):
    blog_detail=get_object_or_404(blog,pk=blog_id )
    return render(request,'blog/detail.html',{'blog_detail':blog_detail})
