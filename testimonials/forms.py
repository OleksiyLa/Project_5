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

    name = forms.CharField(
        label='Name',
        max_length=100,
        required=True,
        error_messages={
            'required': 'Please provide your name for the testimonial.',
            'max_length': 'The name cannot exceed 100 characters.'
        }
    )

    testimonial = forms.CharField(
        label='Testimonial',
        widget=forms.Textarea(attrs={'rows': 10}),
        required=True,
        error_messages={
            'required': 'Please write your testimonial.',
        }
    )

    rating = forms.ChoiceField(
        choices=Testimonial.RATING_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        error_messages={
            'required': 'Please select a rating for the testimonial.'
        }
    )

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        rating_values = [str(choice[0]) for choice in Testimonial.RATING_CHOICES]
        if rating not in rating_values:
            raise forms.ValidationError('Invalid rating value.')
        return rating
