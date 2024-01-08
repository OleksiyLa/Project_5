from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
        }

        self.fields['default_full_name'].widget.attrs['maxlength'] = 50
        self.fields['default_phone_number'].widget.attrs['maxlength'] = 20
        self.fields['default_postcode'].widget.attrs['maxlength'] = 20
        self.fields['default_street_address1'].widget.attrs['maxlength'] = 80
        self.fields['default_street_address2'].widget.attrs['maxlength'] = 80

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-custom'
            self.fields[field].label = False
