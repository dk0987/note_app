from django.shortcuts import render , redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import RegistrationFrom , NoteForm
from .models import Note


def register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationFrom()
    return render(request, 'register.html', {'form': form})

class note_list(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created')

class create_note(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form)
        return super().form_valid(form)

class edit_note(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = '/'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class delete_note(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = '/'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
