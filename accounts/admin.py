from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TblBanner)
admin.site.register(ImageType) 
admin.site.register(Image)
admin.site.register(TopMenu)
admin.site.register(MenuDetail)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductDetailImage)