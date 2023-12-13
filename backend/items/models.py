from django.db import models
from categories.models import Category

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    body = models.TextField()
    email = models.EmailField()
    status = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Item - {}: {}'.format(self.title, self.status)
