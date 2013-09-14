# Create your models here.
class Donation(utils.Model):
	MONEY = 'mo'
	HOURS = 'hr'
	GOODS = 'gd'

	UNIT_CHOICES = (
		(MONEY, 'Money'),
		(HOURS, 'Hours'),
		(GOODS, 'Physical Goods'),
		)

	date = models.DateTimeField()
	unit = models.CharField(max_length=200, choices=UNIT_CHOICES) #could be money, hours, physical goods
	detail = models.CharField(max_length=200) #currency, type of hours, type of good
	amount = models.DecimalField(max_digits=100, decimal_places=2)

