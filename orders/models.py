from django.db import models


"""
6.4.7 Make Choices and Sub-Choices Model Constants
"""
class IceCreamOrder(models.Model):
    FLAVOR_CHOCOLATE = 'ch'
    FLAVOR_VANILLA = 'vn'
    FLAVOR_STRAWBERRY = 'st'
    FLAVOR_CHUNKY_MUNKY = 'cm'

    FLAVOR_CHOICES = (
        (FLAVOR_CHOCOLATE, 'chokolate'),
        (FLAVOR_VANILLA, 'Vanilla'),
        (FLAVOR_STRAWBERRY, 'Strawberry'),
        (FLAVOR_CHUNKY_MUNKY, 'chunky Munky')
    )
    flavor = models.CharField(
        max_length=2,
        choices=FLAVOR_CHOICES)

    """
    Using this model, we can do the following:

    >>> from orders.models import IceCreamOrder
    >>>
    ,→ IceCreamOrder.objects.filter(flavor=IceCreamOrder.FLAVOR_CHOCOLATE)
    [<icecreamorder: 35>, <icecreamorder: 42>, <icecreamorder: 49>]
    """


"""
6.4.7 Make Choices and Sub-Choices Model Constants
"""

# class IceCreamOrder(models.Model):
#     class Flavor(models.TextChoices):
#         CHOCOLATE = 'ch', 'Chocolate'
#         VANILA = 'vn', 'Vanila'
#         STRAWBERRY = 'st', 'Strawberry'
#         CHUNKY_MUNKY = 'cm', 'Chunky Munky'

#     flavor = models.CharField(
#         max_length=2,
#         choices=Flavor.choices
#     )
#     """
#     Using this code we’re able to do:

#     >>> from orders.models import IceCreamOrder
#     >>>
#     ,→ IceCreamOrder.objects.filter(flavor=IceCreamOrder.Flavors.CHOCOLATE)
#     [<icecreamorder: 35>, <icecreamorder: 42>, <icecreamorder: 49>]

#     """
