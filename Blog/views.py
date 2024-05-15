from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Dummy data post=[
#     {
#         'author': 'Ashok gaire',
#         'title':'The Last of us',
#         'description':'survivor wins the game',
#         'date_posted':'November 27,2024',
#     },
#     {
#         'author': 'Arpan paudyal',
#         'title': 'Stranger thing',
#         'description': 'survivor wins the game',
#         'date_posted': 'December 21,2024',
#     }
# ]
def home(request):
    context={
        'posts': Post.objects.all(),
    }
    return render(request,'Blog/home.html',context)

def about(request):
    return render(request,'Blog/about.html',{'title':'About'})


