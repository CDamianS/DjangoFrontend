from django.db import models

# Create your models here.
class Log(models.Model):
    points= models.CharField(max_length= 200)
    date = models.DateTimeField('date added')

    #Esta funcioncita, solo esta formateando para que en la impresion siempre se ve con sus datos donde deben de estar. 
    #Es un formater, que despues nos ayudará a tener buena info.
    def __str__(self):
        return f"Date: {self.date}, points: {self.points}pts"
