from django.shortcuts import render

def about_view(request):
    return render(request, 'about/about.html', {'active_link': 'about'})