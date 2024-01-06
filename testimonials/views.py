from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Value, Case, When, BooleanField
from django.http import Http404
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib import messages


def testimonials_view(request):
    six_testimonials = Testimonial.objects.filter(
        publish_testimonial=True,
        is_verified=True
    ).annotate(
        is_5_star=Case(
            When(rating=5, then=Value(0)),
            default=Value(1),
            output_field=BooleanField()
        )
    ).order_by('is_5_star', 'created_at')[:6]

    return render(request, 'testimonials/testimonials.html', {'active_link': 'testimonials', 'testimonials': six_testimonials})


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        user = request.user
        has_testimonial = Testimonial.objects.filter(user=user, publish_testimonial=True).exists()
        if has_testimonial:
            messages.warning(request, 'You have already left a testimonial. You may be able to leave it after some time.')
            return redirect('testimonials')
        orders = user.userprofile.orders.all()
        if orders.count() > 0:
            form = TestimonialForm(request.POST)
            if form.is_valid():
                testimonial = form.save(commit=False)
                testimonial.user = request.user
                testimonial.save()
                messages.success(request, 'Thank you for your testimonial!')
                return redirect('testimonials')
        else:
            messages.error(request, 'You must have placed an order to leave a testimonial.')
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/add_testimonial.html', {'form': form})


@login_required
def approve_testimonial(request, testimonial_id):
    if not request.user.is_superuser:
        raise Http404('Not found.')
    try:
        testimonial = Testimonial.objects.get(id=testimonial_id)
        testimonial.is_verified = True
        testimonial.save()
        messages.success(request, 'Testimonial approved!')
    except Testimonial.DoesNotExist:
        messages.error(request, 'Testimonial not found.')
    return redirect('not_approved_testimonials')


@login_required
def delete_testimonial(request, testimonial_id):
    if not request.user.is_superuser:
        raise Http404('Not found.')
    try:
        testimonial = Testimonial.objects.get(id=testimonial_id)
        testimonial.delete()
        messages.success(request, 'Testimonial deleted!')
    except Testimonial.DoesNotExist:
        messages.error(request, 'Testimonial not found.')
    return redirect('testimonials')


@login_required
def view_not_approved_testimonials(request):
    if not request.user.is_superuser:
        raise Http404('Not found.')
    testimonials = Testimonial.objects.filter(is_verified=False, publish_testimonial=True).order_by('created_at')
    return render(request, 'testimonials/testimonials.html', {'active_link': 'testimonials', 'testimonials': testimonials})