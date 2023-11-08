from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django_daraja.mpesa.core import MpesaClient
from django_daraja.mpesa.exceptions import MpesaInvalidParameterException

from mpesa import form
from mpesa.form import PaymentForm


# Create your views here.
# def index(request):
#     customer = MpesaClient()
#     phone_number = '011144510'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = customer.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            amount = int(form.cleaned_data['amount'])  # Convert to an integer
            account_reference = 'reference'
            transaction_desc = 'Description'
            callback_url = 'https://api.darajambili.com/express-payment'

            # Initialize the MpesaClient
            customer = MpesaClient()  # You should have this initialized in your code

            # Call the function to process the payment
            try:
                response = customer.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

                # Check the response status or handle success/failure as per the API's documentation
                if response.status_code == 200:
                    return HttpResponse(f"Payment successful for {name}.")
                else:
                    return HttpResponse(f"Payment failed for {name}. Please try again.")
            except MpesaInvalidParameterException as e:
                return HttpResponse(f"Payment failed. {e}")
        else:
            return HttpResponse("Invalid form data. Please check your input.")
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form})