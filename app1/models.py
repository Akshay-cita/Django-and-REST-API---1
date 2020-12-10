from django.db import models

class Artist(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)

	def __str__(self):
		return self.first_name

class Song(models.Model):
	album=models.CharField(max_length=100)
	artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
	description= models.CharField(max_length=200)

	def __str__(self):
		return self.album