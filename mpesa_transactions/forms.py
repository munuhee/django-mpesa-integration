from django import forms
from .models import MPesaTransaction

class MPesaTransactionForm(forms.ModelForm):
    """
    ModelForm for handling M-Pesa transactions.
    """

    class Meta:
        model = MPesaTransaction
        fields = ['phone_number', 'amount', 'account_reference', 'transaction_desc']

    def clean_amount(self):
        """
        Custom validation for the amount field.
        """
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount
