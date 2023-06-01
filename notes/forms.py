from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        labels = {
            'title': 'Note Title',
            'content': 'Note Content'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control my-5'})
        }

    # def clean_title(self):
    #     # used for strong validation e.g. email validation
    #     title = self.cleaned_data.get('title') # cleaned_data is a dictionary which is reurned by the form after validation
    #     if "django" not in title:
    #         raise forms.ValidationError("Title should contain the word django")
    #     return title 