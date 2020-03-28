from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300)
    price = models.FloatField()
    description= models.TextField(default='')
    count= models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id
        }
class Category(models.Model):
    name=models.CharField(max_length=300)


    def to_json(self):
        return{
            'id':self.id,
            'name': self.name
        }