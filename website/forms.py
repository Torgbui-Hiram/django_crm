from django import forms
from django.forms.models import ModelForm
from .models import TodoList


class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ('name', 'user_mail', 'details', 'status', 'due_date')

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['user_mail'].widget.attrs['class'] = 'form-control'
        self.fields['details'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-check'
        self.fields['due_date'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Name of Task'


class SearchForm(forms.Form):
    seach = forms.CharField(max_length=50)





