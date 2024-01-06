from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['rating', 'testimonial', 'publish_testimonial']
        widgets = {
            'testimonial': forms.Textarea(attrs={'rows': 10}),
        }
