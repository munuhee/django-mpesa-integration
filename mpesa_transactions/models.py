import uuid
from django.db import models

class MPesaTransaction(models.Model):
    """
    Model representing an M-Pesa transaction.
    """
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    amount = models.IntegerField(verbose_name="Amount")  # Using DecimalField for better precision
    account_reference = models.CharField(max_length=50, verbose_name="Account Reference")
    transaction_desc = models.CharField(max_length=255, verbose_name="Transaction Description")

    class Meta:
        verbose_name = "M-Pesa Transaction"
        verbose_name_plural = "M-Pesa Transactions"

    def __str__(self):
        """
        String representation of the M-Pesa transaction.
        """
        return f"{self.phone_number} - {self.amount}"
