from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    ModelPortfolio,
    ModelPortfolioHolding,
    ModelPortfolioBench
)
from .serializers import (
    ModelPortfolioSerializer,
    ModelPortfolioHoldingSerializer,
    ModelPortfolioBenchSerializer
)

# Create your views here.
class ModelPortfolioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ModelPortfolio.objects.all()
    serializer_class = ModelPortfolioSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='holding-betas')
    def holding_betas(self, request, pk=None):
        num_days = int(self.request.query_params.get('num_days', 756))
        port = self.get_object()
        betas = port.betas(num_days)
        return Response({'betas': betas})

    @action(detail=True, methods=['get'])
    def corr(self, request, pk=None):
        num_days = int(self.request.query_params.get('num_days', 756))
        port = self.get_object()
        corr = port.corr(num_days)
        holdings = corr.index.to_list()
        data = corr.to_numpy().tolist()
        return Response({'holdings': holdings, 'corr': data})

    @action(detail=True, methods=['get'])
    def cov(self, request, pk=None):
        num_days = int(self.request.query_params.get('num_days', 756))
        port = self.get_object()
        cov = port.cov(num_days)
        holdings = cov.index.to_list()
        data = cov.to_numpy().tolist()
        return Response({'holdings': holdings, 'cov': data})

class ModelPortfolioHoldingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ModelPortfolioHolding.objects.all()
    serializer_class = ModelPortfolioHoldingSerializer
    permission_classes = [IsAuthenticated]


class ModelPortfolioBenchViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ModelPortfolioBench.objects.all()
    serializer_class = ModelPortfolioBenchSerializer
    permission_classes = [IsAuthenticated]