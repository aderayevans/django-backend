from django.db import models

# Create your models here.
class mShark(models.Model):
    intro = "Hello, This is Shark from Django"

    def getIntro(self) -> set[str]:
        return { mShark.intro }

class Accounts(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    create_date  = models.DateTimeField('date published')