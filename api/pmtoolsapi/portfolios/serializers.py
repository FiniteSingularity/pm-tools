from rest_framework import serializers
from .models import ModelPortfolio, ModelPortfolioHolding, ModelPortfolioBench


class ModelPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPortfolio
        fields = ['id', 'name', ]
        read_only_fields = ['id',]


class ModelPortfolioHoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPortfolioHolding
        fields = ['id', 'portfolio', 'holding', 'weight', 'benchmark', ]
        read_only_fields = ['id',]


class ModelPortfolioBenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPortfolioBench
        fields = ['id', 'portfolio', 'benchmark', 'expected_return', ]
        read_only_fields = ['id',]