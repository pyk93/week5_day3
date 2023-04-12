from django.db import models

# Create your models here.

class Photocard(models.Model):
	def __str__(self):
		return f"{self.artist} {self.album}-{self.name}({self.member})"

	name = models.CharField(default="",null=False, max_length=128)
	price = models.IntegerField(default=1000)
	is_limited_edition = models.BooleanField(default=False)

	artist = models.CharField(default="A", null=False, max_length=32)
	member = models.CharField(default="1st",null=False, max_length=32)
	album = models.CharField(default="1st release", null=False, max_length=64)



