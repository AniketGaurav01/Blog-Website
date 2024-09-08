from django.shortcuts import render
from .models import Posts
# Create your views here.
def index(request):
    posts=Posts.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    posts=Posts.objects.get(id=pk)
    return render(request,"post.html",{'posts':posts})