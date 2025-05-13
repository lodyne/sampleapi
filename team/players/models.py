from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Player(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'players'
        verbose_name = "Player"
        verbose_name_plural = "Players"
        ordering = ['name']