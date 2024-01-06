from django.shortcuts import render

def testimonials_view(request):
    return render(request, 'testimonials/testimonials.html', {'active_link': 'testimonials'})
