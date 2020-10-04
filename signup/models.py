from django.db import models


class Customers(models.Model):
    """
    Model representing a customer.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    mobile_number = models.CharField(max_length=11)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
    