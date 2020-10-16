from rest_framework import serializers
from .models import Benchmark

class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = ['id', 'name', 'ticker', ]
        read_only_fields = ['id',]