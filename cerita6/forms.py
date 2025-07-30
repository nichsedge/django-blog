from django import forms

from .models import Event, Member


class formEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class formMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class Todo_Form(forms.Form):
    error_messages = {'required': 'Fill this field!', }

    title_attrs = {'type': 'text', 'class': 'todo-form-input', 'placeholder': 'Add title...'}
    description_attrs = {'type': 'text', 'cols': 50, 'rows': 4, 'class': 'todo-form-textarea',
                         'placeholder': 'Add description...'}

    title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs))
    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs))
