from django.db import models


class AdditionalItemEvent(models.Model):

    item_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    distance = models.ForeignKey(
        'distance_details.DistanceEvent',
        related_name='additional_options',
        on_delete=models.CASCADE, null=False
        )

    def __str__(self):
        return f'{self.get_item_type_display()} - {self.price}'
