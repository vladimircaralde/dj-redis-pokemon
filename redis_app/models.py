from django.db import models


class Element(models.Model):
    element = models.CharField(max_length=100)

    def __str__(self):
        return self.element


class Pokemon(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self) -> str:
        output = f"{self.name} - {self.element}"
        return output
