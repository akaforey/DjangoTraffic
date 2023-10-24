# from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import NotesForm
from .models import TrafficReport


# class NotesDeleteView(LoginRequiredMixin, DeleteView):
#     model = Notes
#     success_url = '/smart/notes'
#     template_name = 'notes/notes_delete.html'
#     login_url = "/login"

# class NotesUpdateView(LoginRequiredMixin, UpdateView):
#     model = Notes
#     success_url = '/smart/notes'
#     form_class = NotesForm
#     login_url = "/login"

# class NotesCreateView(LoginRequiredMixin, CreateView):
#     model = Notes
#     success_url = '/smart/notes'
#     form_class = NotesForm
#     login_url = "/login"

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
        
class TrafficListView(LoginRequiredMixin, ListView):
    model = TrafficReport
    context_object_name = "traffic_list"
    template_name = "traffic/traffic_list.html"
    login_url = "/login"

    def get_queryset(self):
        print(TrafficReport.objects.all())
        return TrafficReport.objects.all()

class TrafficDetailView(LoginRequiredMixin, DetailView):
    model = TrafficReport
    context_object_name = "traffic_detail"
    template_name = "traffic/traffic_detail.html"
    login_url = "/login"