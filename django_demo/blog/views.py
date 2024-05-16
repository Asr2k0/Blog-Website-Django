from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Remove later just testing response from db
post = [
    {
        'author': 'Rithvik',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home(request):
    context = {


        'posts':post
    }
    return render(request,'blog/home.html',context)


def about(request):
    # context = {
    #     ''
    # }
    return render(request,'blog/about.html',{'title': 'About'})