from django.db import models

class Review(models.Model):
    product = models.ForeignKey("api.Product", on_delete=models.CASCADE)    
    rating = models.DecimalField(max_digits=9, decimal_places=2)
    review = models.TextField(max_length=250)

    def __str__(self):
        return str(self.review)
