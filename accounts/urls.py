from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.IndexOgani, name='IndexOgani'),
    path('ShopDetails/', views.ShopDetails, name='ShopDetails'),
    path('ShoppingCart/', views.ShoppingCart, name='ShoppingCart'),
    path('checkout/', views.Checkout, name='Checkout'),
    path('blog/', views.blog, name='blog'),
    path('blogDetail/', views.blogDetail, name='blogDetail'),
    path('shopGrid/', views.ShopGrid, name='shopGrid'),

    path('list-product-api/', list_product_api, name='list-product-api'),

    path('Pros/', ProductsListCreate.as_view(), name='ProList'),
    path('Pros/<int:pk>/', ProductsDetail.as_view(), name='ProDetail'),
    path('categoryLC/', CategoryListCreate.as_view(), name='categories-list-create'),
    path('categoryUD/<int:pk>/', CategoryUpdateDelete.as_view(), name='categories-detail'),

    path('Index', views.Index, name='Index'),
    path('products/', views.products),
    path('customer/', views.customer),
    path('ContactUs/', views.ContactUs,name='ContactUs'),
    path('AboutUs/', views.AboutUs,name='AboutUs'),
    path('Login/', views.Login,name='Login'),
    path('Products/', views.Products,name='Products'),
    path('MenuDetailMethod/<int:pk>/', views.MenuDetailMethod,name='MenuDetailMethod')
]