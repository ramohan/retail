from django.db import models

# Create your models here.

class Master_Data(models.Model):
	serial = models.IntegerField(unique = True)
	Item_category = models.CharField(max_length = 30)
	Item_Sub_Category = models.CharField(max_length = 20)
	Item_Name = models.CharField(max_length = 30)
	Quantity = models.IntegerField()
	Price = models.FloatField()

	def __unicode__(self):
		return unicode(self.Item_Name)



