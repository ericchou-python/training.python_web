from django.db import models

class sales_person(models.Model):
    sales_person_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.sales_person_name 


