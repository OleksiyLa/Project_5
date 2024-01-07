from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect)

    class Meta:
        model = Testimonial
        fields = ['name', 'testimonial', 'rating', 'publish_testimonial']
        labels = {
            'testimonial': 'Please write a testimonial',
            'publish_testimonial': 'Allow your testimonial to be published',
        }
        widgets = {
            'testimonial': forms.Textarea(attrs={'rows': 10}),
        }
