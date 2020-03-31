from django.db import models

# Create your models here.
class App01DimStockUpdowns(models.Model):
    dt_stock_code = models.CharField(max_length=255, blank=True, null=True)
    week_ud = models.CharField(max_length=255, blank=True, null=True)
    month_ud = models.CharField(max_length=255, blank=True, null=True)
    three_month_ud = models.CharField(max_length=255, blank=True, null=True)
    six_month_ud = models.CharField(max_length=255, blank=True, null=True)
    year_ud = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = '涨跌幅'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'app01_dim_stock_updowns'

    def __str__(self):
        return  self.dt_stock_code
