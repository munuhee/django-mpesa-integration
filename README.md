<img src="https://res.cloudinary.com/murste/image/upload/v1713944812/icons/daraja_geyyh9.png" width="200">

# Django M-Pesa Integration

This Django app offers a comprehensive solution for managing M-Pesa transactions within Django applications. It encompasses functionalities such as initiating STK push requests, processing payment notifications, and storing transaction records in the database.

## Features

- **STK Push Requests:** Initiate payments using Safaricom's STK push functionality.
- **Transaction Record Keeping:** Store transaction details in the database for future reference.
- **Easy Integration:** Simple setup and configuration for seamless integration.

## Prerequisites

Before using this app, ensure you have the following:

- Django installed in your environment.
- A Safaricom Developer Portal account.
- Consumer Key and Consumer Secret obtained from the Safaricom Developer Portal.
- Test credentials assigned to you by Safaricom.

## Virtual Environment Setup

1. Create a virtual environment:

    ```bash
    python -m venv myenv
    ```

2. Activate the virtual environment:

    - **For Linux/MacOS:**

    ```bash
    source myenv/bin/activate
    ```

    - **For Windows:**

    ```bash
    myenv\Scripts\activate
    ```

## Installation

1. Install Django and other dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

2. Add `'django_daraja'` and `'mpesa_transactions'` to your `INSTALLED_APPS` in Django settings.

3. Create a `.env` file in the root directory of your Django project and add the following Mpesa Daraja credentials:

    ```dotenv
    MPESA_ENVIRONMENT= # Set to 'sandbox' or 'production'
    MPESA_CONSUMER_KEY= # Your Safaricom Consumer Key
    MPESA_CONSUMER_SECRET= # Your Safaricom Consumer Secret
    MPESA_SHORTCODE= # Your Mpesa Paybill or Till Number
    MPESA_EXPRESS_SHORTCODE= # Your Mpesa Express Paybill or Till Number
    MPESA_SHORTCODE_TYPE= # Set to 'paybill' or 'till_number'
    MPESA_PASSKEY= # Your Mpesa Passkey
    MPESA_INITIATOR_USERNAME= # Your Mpesa Initiator Username
    MPESA_INITIATOR_SECURITY_CREDENTIAL= # Your Mpesa Initiator Security Credential
    ```

4. Update your Django settings to load environment variables from the `.env` file. For example:

    ```python
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Mpesa Daraja credentials
    MPESA_ENVIRONMENT = os.getenv('MPESA_ENVIRONMENT')
    MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
    MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
    MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
    MPESA_EXPRESS_SHORTCODE = os.getenv('MPESA_EXPRESS_SHORTCODE')
    MPESA_SHORTCODE_TYPE = os.getenv('MPESA_SHORTCODE_TYPE')
    MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
    MPESA_INITIATOR_USERNAME = os.getenv('MPESA_INITIATOR_USERNAME')
    MPESA_INITIATOR_SECURITY_CREDENTIAL = os.getenv('MPESA_INITIATOR_SECURITY_CREDENTIAL')
    ```

5. Depending on your operating system, run the appropriate command to source the `.env` file:

    - **For Linux/MacOS:**

    ```bash
    source .env
    ```

    - **For Windows:**

    ```bash
    call setenv.bat
    ```

6. Run migrations to create the necessary database tables.

## Usage

1. **Sending STK Push Requests:**
   - Visit the homepage of the Django application `localhost:8000`.
   - Fill out the form with the required details: phone number, amount, account reference, and transaction description.
   - Click on the "Pay Now" button to initiate the payment.

2. **Retrieving Transaction Records:**
   - To view transaction records, visit `localhost:8000/records`.
   - All transaction records will be displayed in a tabular format.

## Acknowledgments

- Thanks to [Safaricom](https://www.safaricom.co.ke/) for providing the M-Pesa API.
- This project is inspired by the need for seamless M-Pesa integration in Django applications.
