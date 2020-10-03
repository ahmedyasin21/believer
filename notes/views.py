from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from .models import Notes
from .forms import NotesForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth



class NotesListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes_data'
    paginate_by = 15
    def get_queryset(self):
        user = get_object_or_404(auth.models.User, username=self.kwargs.get('username'))
        return Notes.objects.filter(author=user).order_by('-create_date')

class NotesCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    form_class = NotesForm
    model = Notes
    template_name = "notes/notes_create.html"

    def form_valid(self, form,*args, **kwargs):
        form.instance.author = self.request.user
        return super(*args, **kwargs).form_valid(form)
    
    


class NotesDetailView(LoginRequiredMixin,DetailView):
    login_url = '/accounts/login/'
    model = Notes
    context_object_name = 'notes'
    
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/accounts/login/'
    model = Notes
    success_url = reverse_lazy('notes:notes_list')

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    refirect_field_name ='notes/notes_detail.html'
    form_class = NotesForm
    model = Notes
    template_name = "notes/notes_create.html"