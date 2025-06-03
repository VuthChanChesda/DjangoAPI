from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class TblBanner(models.Model):
    BannerName = models.CharField(max_length=200, null=True)
    BannerImage = models.ImageField(upload_to='images/',null=True,blank=True)
    BannerDate = models.DateTimeField(auto_now_add=True, null=True)

class ImageType(models.Model): 
    ImageTypeName = models.CharField(max_length=200, null=True) 
    ImageTypeDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.id} {self.ImageTypeName}'
    
class Image(models.Model): 
    ImageName = models.CharField(max_length=200, null=True) 
    ImageURL = models.ImageField(upload_to='images/',null=True,blank=True) 
    ImageLink = models.CharField(max_length=200, null=True) 
    ImageTypeID = models.ForeignKey(ImageType, on_delete=models.CASCADE, null=True) 
    Active = models.CharField(max_length=200, null=True) 
    ImageDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.ImageName}'

class TopMenu(models.Model):
    topMenuNameKH = models.CharField(max_length=200, null=True)
    topMenuNameEN = models.CharField(max_length=200, null=True)
    OrderBy = models.IntegerField(blank=True,null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f'{self.id} | {self.topMenuNameKH} | {self.topMenuNameEN} | {self.CreatedDate}'

class MenuDetail(models.Model):
    MenuID = models.ForeignKey(TopMenu, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    MenuDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):         
        return self.MenuID.topMenuNameEN
  

class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    categoryImage = models.ImageField(upload_to='images/Categories/',null=True,blank=True)
    def __str__(self):         
        return self.categoryName
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)
    productDescript =  RichTextUploadingField(null=True)
    weight = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    shipping = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.productName

class ProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    Information = RichTextUploadingField(null=True)
    Reviews = RichTextUploadingField(null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):         
        return self.productDetailName

class ProductDetailImage(models.Model):
    productDetailImageName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    productDetailImage = models.ImageField(upload_to='images/productDetail/',null=True,blank=True)
    imageDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.productDetailImageName