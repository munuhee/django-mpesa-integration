# Generated by Django 5.0.4 on 2024-04-23 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_transactions', '0003_alter_mpesatransaction_checkout_request_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='checkout_request_id',
        ),
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='customer_message',
        ),
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='merchant_request_id',
        ),
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='response_code',
        ),
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='response_description',
        ),
        migrations.RemoveField(
            model_name='mpesatransaction',
            name='timestamp',
        ),
    ]
