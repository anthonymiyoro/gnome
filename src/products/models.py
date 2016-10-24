from django.core.urlresolvers import reverse
from django.db import models



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    car_year = models.CharField(max_length=120)
    car_manufacturer = models.CharField(max_length=120)
    car_type = models.CharField(max_length=120)
    car_model = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk":self.pk})