from django.db import models
from .category import Category
from .brand import Brand
from .size import Size
from .vendor import Vendor
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField 



class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount_price = models.DecimalField(max_digits=9, decimal_places=2, default=20.00)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, default=1)
    free_shipping = models.BooleanField(default=False)
    description = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus quos cupiditate tenetur. Qui labore voluptate nostrum cum! Non inventore possimus fugiat architecto quia laboriosam dolores harum aspernatur tempora nobis. Consectetur.')
    size = models.ManyToManyField(Size)
    trending = models.BooleanField(default=False)
    main_image = CloudinaryField('image',default="img.url")
    side_image = CloudinaryField('image', default="img.url")
    rear_image = CloudinaryField('image', default="img.url")
    
    def __str__(self):
        return self.name
        
    
    
@receiver(pre_delete, sender=Product)
def photo_delete(sender, instance, **kwargs):
    '''Delete image associated to table '''
    cloudinary.uploader.destroy(instance.main_image.public_id)
    cloudinary.uploader.destroy(instance.side_image.public_id)
    cloudinary.uploader.destroy(instance.rear_image.public_id)
    
