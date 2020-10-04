from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .models import Customers


# def signupFrom(request):
#     """
#     signup form View
#     """
#     return HttpResponse("hello every body!")


class CustomersCreateView(CreateView):
    model = Customers
    fields = '__all__'
    success_url = reverse_lazy('signup:success-customer')


class SuccussCreateCustomerView(TemplateView):
    template_name = "signup/success_signup.html"

