from django.contrib import admin
from .models import MPesaTransaction

class MPesaTransactionAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'amount', 'account_reference', 'transaction_desc')
    search_fields = ['phone_number', 'account_reference', 'transaction_desc']
    list_filter = ['phone_number', 'amount']

admin.site.register(MPesaTransaction, MPesaTransactionAdmin)
