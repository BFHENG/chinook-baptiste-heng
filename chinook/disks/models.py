from django.db import models

class Track (models.Model) : 
    
    name = models.CharField(max_length = 200)
    composer = models.CharField(max_length = 200)
    milliseconds = models.IntegerField()
    
    bytes = models.IntegerField()
    
    unitprice = models.FloatField()

    album = models.ForeignKey('Album', on_delete = models.CASCADE)      #quand on détruit un album, on détruit les tracks associés
    
    def __str__(self):
        return self.name
    
class Album (models.Model):
    
    title = models.CharField(max_length = 200)
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

class Artist (models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

# Create your models here.
