from django import forms

from cerita5.models import Course


class CourseForm(forms.ModelForm):
    # content = forms.CharField()

    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
