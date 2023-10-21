from django.db import models
from django.conf import settings

# property inputs
class Property(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    size = models.IntegerField()    # sq feet living area
    year_built = models.IntegerField()

    def property_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year_built

    def validate_address(self):
        # response = requests.get(f"https://api.example.com/validate_address?address={self.address}")
        # return response.json().get("is_valid", False)
        pass


# quote outputs
class Quote(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    quote_date = models.DateTimeField(auto_now_add=True)
    quote_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_latest = models.BooleanField(default=True)