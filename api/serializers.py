from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','Customer','balance']
        model = Account
