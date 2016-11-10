from django.contrib import admin
from adminfilters.models import ProductListFilter

from src.products.models import ProductListFilter


class ProductListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Products'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'products'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_species = []
        queryset = Species.objects.all()
        for species in queryset:
            list_of_species.append(
                (str(species.id), species.name)
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(species_id=self.value())
        return queryset

    def value(self):
        """
        Overriding this method will allow us to always have a default value.
        """
        value = super(ProductListFilter, self).value()
        if value is None:
            if self.default_value is None:
                # If there is at least one Species, return the first by name. Otherwise, None.
                first_species = ProductListFilter.objects.order_by('name').first()
                value = None if first_species is None else first_species.id
                self.default_value = value
            else:
                value = self.default_value
        return str(value)

