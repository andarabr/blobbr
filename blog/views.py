from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html', {'title' : 'Home'})

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})