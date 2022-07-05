from django.db import models

# Create your models here.
class mShark(models.Model):
    intro = "Hello, This is Shark from Django"

    def getIntro(self) -> set[str]:
        return { mShark.intro }