from django.shortcuts import render
from . models import Post

# Create your views here.
#posts = [
#   {
#        'author':'alok',
#       'title':'Blog post 1',
#       'content':'This content is for post 1.',
#    },
#    {
#       'author':'suresh',
#      'title':'Blog post 2',
#     'content':'This content is for post 2.',
#   },
#   {
#       'author':'ravi',
#        'title':'Blog post 3',
#       'content':'This content is for post 3.',
#   },
#]
def index(request):
    context={'p': Post.objects.all() }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})