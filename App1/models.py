from django.db import models

# Create your models here.

class contact_details(models.Model):
    Name = models.CharField(max_length=50,null=False,blank=False)
    Email = models.EmailField(max_length=25,null=False,blank=False,unique=True)
    Msg = models.TextField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.Email
    
class main_page_email(models.Model):
    Email = models.EmailField(max_length=50,unique=True,null=True,blank=True)

    def __str__(self):
        return self.Email

class blog_main(models.Model):
    author = models.CharField(max_length=15,null=False,blank=False)
    img = models.ImageField(null=False,blank=False,upload_to='blog_img')
    date = models.DateTimeField()
    view = models.PositiveIntegerField(default=0)
    additional_point = models.TextField(max_length=80,null=False,blank=False)
    details = models.TextField(max_length=900000,null=False,blank=False,default='InDetail')

    def __str__(self):
        return self.author
    
# pending /-------------------------------------------------------------
class latest(models.Model):
    lat_author = models.CharField(max_length=15,null=False,blank=False)
    lat_img = models.ImageField(null=False,blank=False,upload_to='blog_img')
    lat_date = models.DateTimeField()
    lat_view = models.PositiveIntegerField(default=0)
    lat_additional_point = models.TextField(max_length=80,null=False,blank=False)
    lat_details = models.TextField(max_length=900000,null=False,blank=False,default='Latest')
    def __str__(self):
        return self.lat_author


class slider(models.Model):
    sli_first = models.ImageField(upload_to='slider_img',null=False,blank=False)
    first_additional_point = models.TextField(max_length=80,null=False,blank=False)
    first_detail = models.TextField(max_length=900000,null=False,blank=False,default='First Slider')
    sli_second = models.ImageField(upload_to='slider_img',null=False,blank=False)
    second_additional_point = models.TextField(max_length=80,null=False,blank=False)
    second_detail = models.TextField(max_length=900000,null=False,blank=False,default='Second Slider')
    sli_third = models.ImageField(upload_to='slider_img',null=False,blank=False)
    third_additional_point = models.TextField(max_length=80,null=False,blank=False)
    third_detail = models.TextField(max_length=900000,null=False,blank=False,default='Third Slider')

    def __str__(self):
        return self.first_additional_point 
    
