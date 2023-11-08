
from django import forms

from mpesa.models import Payment


class PaymentForm(forms.Form):
    name = forms.CharField(label='Your Name')
    phone_number = forms.CharField(label='Phone Number')
    amount = forms.DecimalField(label='Amount to Pay', min_value=1)

