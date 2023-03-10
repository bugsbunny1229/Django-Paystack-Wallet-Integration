from django.contrib import admin
from .models import Wallet, WalletTransaction

admin.site.register(Wallet)
admin.site.register(WalletTransaction)