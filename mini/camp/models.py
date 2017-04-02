from django.db import models
from address.models import District
from rrc.models import Rrc
# Create your models here.
class Camp(models.Model):
	name = models.CharField(max_length=15, null=False, unique=True)
	district = models.ForeignKey(District)
	rrc = models.ForeignKey(Rrc, null=True, blank=True)
	address = models.TextField(null=True)
	date = models.DateTimeField(null=True)
	contact = models.CharField(max_length=25, null=False)

	def __str__(self):
		return self.name+' ----- '+str(self.district)+' ----- '+str(self.rrc)+' ----- '+str(self.date)