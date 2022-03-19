from logging import getLogger

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from viewer.forms import CarForm
from viewer.models import Cars

LOG = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


def search(request):
    title = request.GET.get("movie_title")
    # if title:
    #     data = Movie.objects.filter(title__contains=title)
    #     return render(request, "search.html", context={'data': data, 'count': data.count(), 'movie_title': title})
    # return render(request, "search.html", context={'data': None, 'count': 0, 'movie_title': ''})


# def home(request):
#     return render(request, "home.html")


# class HomeView(TemplateView):
#     template_name = "index.html"


# def contact(request):
#     return render(request, "contact.html")


# class ContactView(TemplateView):
#     template_name = "contact.html"


class HomeView(TemplateView):
    template_name = "index.html"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a movie.")
        return super().form_invalid(form)


class CarsView(ListView):
    template_name = "cars.html"
    model = Cars


class SingleCarView(DetailView):
    template_name = "car_detail_view.html"
    model = Cars


class CarCreateView(CreateView):
    template_name = 'forms/form.html'
    form_class = CarForm
    success_url = reverse_lazy('index')

    # permission_required = "viewer.create_car"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)


class CarDetailView(DetailView):
    template_name = "car_detail_view.html"
    model = Cars


class CarUpdateView(
    # PermissionRequiredMixin,
    StaffRequiredMixin, UpdateView):
    template_name = "forms/form.html"
    form_class = CarForm
    model = Cars
    success_url = reverse_lazy('viewer:cars')
    # permission_required = "viewer.change_car"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a movie.")
        return super().form_invalid(form)


class CarDeleteView(
    # PermissionRequiredMixin,
    StaffRequiredMixin, DeleteView):
    template_name = "forms/delete_car_form.html"
    model = Cars
    success_url = reverse_lazy('viewer:cars')
    # permission_required = "viewer.delete_car"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser