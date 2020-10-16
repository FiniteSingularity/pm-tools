from rest_framework import serializers
from .models import Symbol, Price

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ['id', 'ticker', 'short_name', 'long_name', 'source', ]
        read_only_fields = ['id', 'short_name', 'long_name',]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [
            'date',
            'open_price',
            'close_price',
            'high_price',
            'low_price',
            'adjusted_close',
            'volume']
