from django.db import models

# Create your models here.
class BookModels(models.Model){
  name = models.Charfield(max_length=100)
  author = models.Charfield(max_length=100)
}
