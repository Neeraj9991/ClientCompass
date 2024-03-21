from django.db import models


class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    # Source from which the lead was generated (e.g., website, referal, advertisement)
    lead_source = models.CharField(max_length=100, blank=True, null=True)

    # Type of customer (e.g., individual, corporate)
    customer_type = models.CharField(max_length=100, blank=True, null=True)

    # Current status of the customer (e.g., active, inactive)
    status = models.CharField(max_length=100, blank=True, null=True)

    # Allow for optional notes
    notes = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
