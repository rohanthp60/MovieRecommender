from django.db import models

class Movies(models.Model):
    key = models.CharField(max_length=255, unique=True) 
    value1 = models.IntegerField()                      
    value2 = models.IntegerField()                       
    value3 = models.IntegerField()                       
    value4 = models.IntegerField()                       
    value5 = models.IntegerField()  
    value6 = models.IntegerField()                     

    def set_values(self, name, values):
        self.value1, self.value2, self.value3, self.value4, self.value5, self.value6 = values
        self.key = name

    def get_values(self):
        return [self.value1, self.value2, self.value3, self.value4, self.value5, self.value6]



