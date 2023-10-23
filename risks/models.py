from django.db import models
from django.conf import settings


class Risk(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    size = models.IntegerField()    # sq feet living area
    year_built = models.IntegerField()

    def risk_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year_built

    def validate_address(self):
        # response = requests.get(f"https://api.example.com/validate_address?address={self.address}")
        # return response.json().get("is_valid", False)
        pass
        
    def display(self):
        message = "Address: " + self.address + \
                ", Living Area: " + str(self.size) + \
                ", Year Built: " + str(self.year_built)
        return message
