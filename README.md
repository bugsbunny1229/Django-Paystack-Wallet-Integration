# Django Paystack Wallet Integration

A Django-based digital wallet application that seamlessly integrates with Paystack for secure payment processing and transaction management.

## 🚀 Features

- 🏦 User Wallet Management
  - Create and manage digital wallets
  - Support for multiple currencies (default: NGN)
  - Secure user authentication

- 💳 Payment Processing
  - Integration with Paystack payment gateway
  - Secure deposit transactions
  - Real-time transaction status updates

- 📊 Transaction Management
  - Track all wallet transactions
  - Detailed transaction history
  - Timestamps and status tracking

## 🛠️ Technology Stack

- Backend: Django
- Payment Gateway: Paystack
- Database: SQLite (default)
- Authentication: Django's built-in User model

## 📋 Prerequisites

- Python 3.8+
- Django
- Paystack API credentials

## 🚀 Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django
   pip install python-dotenv
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Paystack credentials
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 📝 Usage

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Access the admin panel at `/admin`
3. Create wallets and process transactions through the API endpoints

## 🛠️ API Endpoints

- `/api/wallet/` - Wallet management
- `/api/transactions/` - Transaction management
- `/api/deposit/` - Process deposits

## 🙏 Acknowledgments

- Paystack for their excellent payment gateway service
- Django community for their amazing framework
