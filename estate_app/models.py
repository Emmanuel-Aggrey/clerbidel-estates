from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.
class Basemodel(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True

class Propertytype(Basemodel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True, null=True)
    image = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True,help_text='optional')

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'property'

    def __str__(self):
        return self.name


class Property(Basemodel):
    property_type = models.ForeignKey(Propertytype,on_delete=models.CASCADE,related_name='properties')
    name = models.CharField(max_length=200,blank=True, null=True,help_text='eg single room,story building')
    price = models.DecimalField(decimal_places=2,max_digits=50,blank=True, null=True)
    location = models.CharField(max_length=200,blank=True, null=True)
    slug = models.SlugField(unique=True,blank=True, null=True)

    description = models.TextField(blank=True,null=True)
    bed = models.PositiveSmallIntegerField(blank=True, null=True)
    bath = models.PositiveSmallIntegerField(blank=True, null=True)
    sqrt = models.CharField(max_length=20,blank=True, null=True)
    sale_type = (
    ('rent','RENT'),
    ('sale','SALE'),
    ('sale or rent','SALE or RENT')
    )
    sale_type = models.CharField(max_length=20,choices=sale_type,blank=True, null=True,default='sale')
    available = models.BooleanField(default=True)

    image = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    image1 = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    image2 = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    image3 = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    image4 = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    image5 = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True, null=True)
    # work on this two duplicate
    # have fixed it but have to safe phone number befor a user is allowed to upload a property in views.py
    # for now duplicates
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
<<<<<<< HEAD


=======
    user_phone = models.CharField(max_length=15,blank=True, null=True)
 
    
>>>>>>> cecbcc0aadf69c6bbba0fb1eb4d2cf4ca8113de0
    def __str__(self):
        return '{} {}'.format(self.name,str(self.property_type))

    def get_absolute_url(self):

        return reverse('estate_app:detailpage', args=[self.id])

    def delete(self, *args, **kwargs):

        if self.image or  self.image1 or self.image2 or self.image3 or self.image4 or self.image5:
            self.image1.delete()
            self.image2.delete()
            self.image3.delete()
            self.image4.delete()
            self.image5.delete()
        super().delete(*args, **kwargs)




class Agent(Basemodel):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='profiles/%Y/%m/%d/',blank=True, null=True)
    position = models.CharField(max_length=200,blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url  = models.URLField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'
        ordering  =['-date_updated']

class Phone(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userphone')
    phonenumber =models.CharField(max_length=15,blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Gallary(models.Model):
    name = models.TextField('about',blank=True, null=True,help_text='enter something about this image')
    image = models.FileField(upload_to='gallary/%Y/%m/%d/')
