from django.db import models

class Manufacture(models.Model):
    manufacture_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.manufacture_name 


class Product(models.Model):
    product_manufacture = models.ForeignKey(Manufacture)
    product_desc = models.TextField()
    product_date = models.DateField(auto_now=True)
    product_price_euro = models.FloatField()
    product_price_nt = models.FloatField()
    product_stock = models.IntegerField()
    product_url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.product_desc
