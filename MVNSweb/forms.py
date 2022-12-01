from django import forms
from .models import Reading

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = [
            'motorist_first_name',
            'motorist_middle_initial',
            'motorist_last_name',
            'plate_number',
            'db_reading',
            'distance_reading',
        ]
