from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Note
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import NoteForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

class NoteSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("notes_list.html")
        return super().get(request, *args, **kwargs)

class NoteLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = '/login'

class NoteLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('notes_list')  # Replace 'notes_list' with the name of your URL pattern for the notes list page

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me', False)
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes'
    template_name = 'notes_delete.html'
    login_url = '/login'

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_update.html'
    success_url = '/notes'
    login_url = '/login'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_create.html'
    login_url = '/login'
    success_url = '/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())

class NoteListView(LoginRequiredMixin, ListView):
    model = Note # this is the model that will be used to fetch the data
    context_object_name = 'notes' # this is the name of the variable that will be used in the template
    template_name = 'notes_list.html' # this is the name of the template that will be used to render the view
    login_url = '/login' # this is the url that will be used to redirect the user if he is not logged in

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes_details.html'
    login_url = '/login'
    

class NoteWelcomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs): # this is how you pass data to the template
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now() 
        return context


