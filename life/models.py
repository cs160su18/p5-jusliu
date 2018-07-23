from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)

class Clothing(models.Model):
  brand_name = models.CharField(max_length=50)
  product_name = models.CharField(max_length=50)
  size = models.CharField(max_length=50)
  color = models.CharField(max_length=50)

class Outfit(models.Model):
  top = models.ForeignKey(Clothing, related_name='top', on_delete=models.CASCADE)
  bottom = models.ForeignKey(Clothing, related_name='bottom', on_delete=models.CASCADE)
  shoes = models.ForeignKey(Clothing, related_name='shoes', on_delete=models.CASCADE)
  hat = models.ForeignKey(Clothing, related_name='hat', on_delete=models.CASCADE)
  jacket = models.ForeignKey(Clothing, related_name='jacket', on_delete=models.CASCADE)

class Post(models.Model):
  title = models.CharField(max_length=50)
  outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
  author_name = models.CharField(max_length=50)
  author_email = models.CharField(max_length=50)
  created = models.DateTimeField(auto_now_add=True)