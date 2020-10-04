from django.urls import path

from . import views


app_name = 'signup'
urlpatterns = [
    path("", views.CustomersCreateView.as_view(), name="create-customer"),
    path("success/", views.SuccussCreateCustomerView.as_view(), name="success-customer"),
]
