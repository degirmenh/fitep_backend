from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.deletion import CASCADE

from django.contrib.gis.db import models as gmodels

from cities.models import Country, Region, City
from account.models import Account


class UserLocation(models.Model):
    user = models.ForeignKey(Account, on_delete=CASCADE, related_name='addresses')
    country = models.ForeignKey(Country, on_delete=CASCADE)
    region = models.ForeignKey(Region, on_delete=CASCADE)
    city = models.ForeignKey(City, on_delete=CASCADE)
    post_code = models.CharField(max_length=25, blank=True, null=True)
    address_1 =  models.CharField(_('address'), max_length=255)
    address_2 =  models.CharField(_("address cont'd"), max_length=255, blank=True)

    is_main_location = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    updated_at = models.DateTimeField(blank=True, null=True, default=None)  
    created_at = models.DateTimeField(auto_now_add=True)  # time saved on db

    def __str__(self) -> str:
        return f'{self.user} {self.country.name} {self.city.name}'




