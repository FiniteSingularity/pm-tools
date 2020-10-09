from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Symbol
from .serializers import SymbolSerializer

# Create your views here.
class SymbolViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
    permission_classes = [IsAuthenticated]