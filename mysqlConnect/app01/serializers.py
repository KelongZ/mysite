from app01 import models
from rest_framework import serializers

class UpdownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.App01DimStockUpdowns
        fields = ('dt_stock_code', 'week_ud', 'month_ud', 'three_month_ud', 'six_month_ud', 'year_ud')