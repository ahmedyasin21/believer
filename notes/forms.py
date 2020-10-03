from django import forms 
from django.views.generic import CreateView,ListView,DetailView
from .models import Notes

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ("title","essay")

        widgets ={
            'title' :forms.TextInput(attrs={'class':'form-control'}),
            'essay':forms.Textarea(attrs={'class':'form-control'})
        }




    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['essay'].label = 'Text'
