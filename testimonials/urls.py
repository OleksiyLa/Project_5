from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials_view, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
]