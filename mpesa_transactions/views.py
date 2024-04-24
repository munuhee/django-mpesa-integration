from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .forms import MPesaTransactionForm
from .models import MPesaTransaction
from django.conf import settings
import base64
import hashlib
from datetime import datetime

def index(request):
    if request.method == 'POST':
        form = MPesaTransactionForm(request.POST)
        if form.is_valid():
            # Extracting form data
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            account_reference = form.cleaned_data['account_reference']
            transaction_desc = form.cleaned_data['transaction_desc']

            # Logic to send STK push request
            cl = MpesaClient()
            business_short_code = settings.MPESA_SHORTCODE
            callback_url = 'https://api.darajambili.com/express-payment'
            data_to_hash = f"{business_short_code}{settings.MPESA_PASSKEY}".encode('utf-8')
            hashed_data = hashlib.sha256(data_to_hash).hexdigest()

            # Sending STK push request
            response = cl.stk_push(
                phone_number,
                amount,
                account_reference,
                transaction_desc,
                callback_url,
            )

            # Save transaction to the database
            form.save()

            return HttpResponse(response)
    else:
        form = MPesaTransactionForm()

    return render(request, 'mpesa_transactions/index.html', {'form': form})

def records(request):
    try:
        transaction_records = MPesaTransaction.objects.all()
    except MPesaTransaction.DoesNotExist:
        transaction_records = None
    except Exception:
        transaction_records = None

    context = {'transaction_records': transaction_records}
    return render(request, 'mpesa_transactions/records.html', context)
