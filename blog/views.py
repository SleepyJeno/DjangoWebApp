from django.shortcuts import render

posts = [
    {
        'author': 'Correy',
        'title': 'Blog Post 1',
        'content': 'First post conent',
        'date_posted': '25 Sep 2021'
    },
    {
        'author': 'Mac',
        'title': 'Blog Post 2',
        'content': 'Second post conent',
        'date_posted': '25 Dec 2021'  
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})