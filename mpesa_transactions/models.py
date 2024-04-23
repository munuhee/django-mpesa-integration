import uuid
from django.db import models

class MPesaTransaction(models.Model):
    """
    Model representing an M-Pesa transaction.
    """

    #merchant_request_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Merchant Request ID")
    #checkout_request_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Checkout Request ID")
    #response_code = models.CharField(max_length=10, verbose_name="Response Code", db_index=True)
    #response_description = models.CharField(max_length=255, verbose_name="Response Description")
    #customer_message = models.CharField(max_length=255, verbose_name="Customer Message")
    #timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")

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
        return f"{self.merchant_request_id} - {self.response_code}"
