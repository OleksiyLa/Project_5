from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm


def testimonials_view(request):
    return render(request, 'testimonials/testimonials.html', {'active_link': 'testimonials'})


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/add_testimonial.html', {'form': form})

