from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'description', 'pages', 'price', 
            'published_date', 'cover', 'website', 'email', 'is_published'
        ]
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
