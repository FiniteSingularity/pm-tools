from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .models import Benchmark
from .serializers import BenchmarkSerializer

# Create your views here.
class BenchmarkViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Benchmark.objects.all()
    serializer_class = BenchmarkSerializer
    permission_classes = [IsAuthenticated]
