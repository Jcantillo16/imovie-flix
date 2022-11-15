from django.db import models

class User (models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50, unique=True)
    password= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    is_login = models.BooleanField(default=False)





    def __str__(self):
        return self.email

    class Meta:
        db_table= 'user'
