from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

posts =[
    {
        'author':'Daim',
        'title':'First Blog',
        'content': 'First blog for the site',
        'date_posted': '15/07/2022'
    }
]

@login_required
def home(request):
    cont = {
        'posts': Post.objects.all,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', cont)