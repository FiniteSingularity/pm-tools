from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Symbol
from .serializers import SymbolSerializer, PriceSerializer
from .utils import make_symbol_from_yahoo

# Create your views here.
class SymbolViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'ticker'

    def create(self, request, *args, **kwargs):
        data = request.data
        ticker_symbol = data['ticker']
        source = data['source']
        if source == Symbol.YAHOO:
            symbol = make_symbol_from_yahoo(ticker_symbol)
        elif source == Symbol.QUANDL:
            # Call function to create symbol from Quandl data.
            pass
        serializer = SymbolSerializer(symbol, many=False)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'])
    def history(self, request, ticker=None):
        ticker = self.get_object()
        start_date = self.request.query_params.get('start_date', '1900-01-01')
        end_date = self.request.query_params.get('end_date', '2400-01-01')
        data_format = self.request.query_params.get('data_format', 'objects')
        price_history = ticker.price_history.filter(
            date__gte=start_date, date__lte=end_date
        ).order_by('date')

        if data_format == 'objects':
            price_serializer = PriceSerializer(price_history, many=True)
            price_data = price_serializer.data
        elif data_format == 'arrays':
            price_data = [
                [
                    ph.date,
                    ph.open_price,
                    ph.low_price,
                    ph.high_price,
                    ph.close_price,
                    ph.volume,
                    ph.adjusted_close
                ] for ph in price_history
            ]
        return Response({'price': price_data})
