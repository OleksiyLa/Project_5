from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib import messages


def testimonials_view(request):
    return render(request, 'testimonials/testimonials.html', {'active_link': 'testimonials'})


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            print("valid", form.cleaned_data)
            messages.success(request, 'Thank you for your testimonial!')
            return redirect('testimonials')
        else:
            messages.error(request, 'Form is invalid.')
            print("error", form.cleaned_data)
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/add_testimonial.html', {'form': form})

