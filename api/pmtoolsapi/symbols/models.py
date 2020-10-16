from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.

class Symbol(models.Model):
    YAHOO = 'Y'
    QUANDL = 'Q'
    SOURCE_CHOICES = [
        (YAHOO, 'Yahoo!'),
        (QUANDL, 'Quandl')
    ]
    ticker = models.CharField(max_length=32, unique=True)
    short_name = models.CharField(max_length=64)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=4, choices=SOURCE_CHOICES, default=YAHOO,)

    def __str__(self):
        return self.ticker


class Price(models.Model):
    ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='price_history')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=8, decimal_places=2)
    close_price = models.DecimalField(max_digits=8, decimal_places=2)
    high_price = models.DecimalField(max_digits=8, decimal_places=2)
    low_price = models.DecimalField(max_digits=8, decimal_places=2)
    adjusted_close = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.BigIntegerField()

    objects = DataFrameManager()

    def __str__(self):
        return f'{self.date}- O:${self.open_price}, H:${self.high_price}, L:${self.low_price}, C:${self.close_price}, AC:${self.adjusted_close}, V:{self.volume}'