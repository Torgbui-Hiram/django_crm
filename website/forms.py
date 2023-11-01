from django import forms
from django.forms.models import ModelForm
from .models import TodoList, Products, Managers, Departments


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


# Serching for items
class SearchForm(forms.Form):
    seach = forms.CharField(max_length=50)


# Adding Product from website
class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'price', 'details', 'authorise_by')

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        # Setting labels to nothing
        self.fields['name'].label = ''
        self.fields['price'].label = ''
        self.fields['details'].label = ''
        self.fields['authorise_by'].label = ''
        # Adding placehoder text to the input fields
        self.fields['name'].widget = forms.TextInput(
            attrs={'placeholder': 'Enter product name', 'class': 'form-control'})
        self.fields['price'].widget = forms.TextInput(
            attrs={'placeholder': 'Product price', 'class': 'form-control'})
        self.fields['details'].widget = forms.Textarea(
            attrs={'placeholder': 'Product descriptions and info', 'class': 'form-control', 'rows': 3})


# Adding manager from website form
class AddManagerForm(ModelForm):
    class Meta:
        model = Managers
        fields = ('title', 'first_name', 'last_name',
                  'department', 'position',)

    def __init__(self, *args, **kwargs):
        super(AddManagerForm, self).__init__(*args, **kwargs)
        # Setting all the labels to empty
        self.fields['title'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['department'].label = ''
        self.fields['position'].label = ''
        # Adding placeholder text to the input fields
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter firstName'})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter lastName'})
        self.fields['position'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter manager position'})


# Adding departments from website
class AddDepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = ('name', 'duties')

    def __init__(self, *args, **kwargs):
        super(AddDepartmentForm, self).__init__(*args, **kwargs)
        # Setting lebels to empty string
        self.fields['name'].label = ''
        self.fields['duties'].label = ''
        # Adding placeholder text to input fields
        self.fields['name'].widget = forms.TextInput(
            attrs={'placeholder': 'Department name', 'class': 'form-control'})
        self.fields['duties'].widget = forms.Textarea(
            attrs={'placeholder': 'Description on the department', 'class': 'form-control', 'rows': 2})
