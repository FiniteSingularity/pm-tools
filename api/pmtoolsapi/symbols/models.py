from django.db import models

# Create your models here.

class Symbol(models.Model):
    YAHOO = 'Y'
    QUANDL = 'Q'
    SOURCE_CHOICES = [
        (YAHOO, 'Yahoo!'),
        (QUANDL, 'Quandl')
    ]
    ticker = models.CharField(max_length=32)
    short_name = models.CharField(max_length=64)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=4, choices=SOURCE_CHOICES, default=YAHOO,)


class Price(models.Model):
    ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='price_history')
    date = models.DateField()
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    adjusted_close = models.IntegerField()
    volume = models.IntegerField()