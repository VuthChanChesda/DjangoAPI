from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from rest_framework import generics
from .serializers import ProductSerializer , CategorySerializer
# Create your views here.

def IndexOgani(request):    
    return render(request, 'Ogani/Index.html')

def ShopDetails(request):    
    return render(request, 'Ogani/shop-details.html')

def ShoppingCart(request):    
    return render(request, 'Ogani/shoping-cart.html')

def Checkout(request):    
    return render(request, 'Ogani/checkout.html')

def blog(request):    
    return render(request, 'Ogani/blog.html')

def blogDetail(request):    
    return render(request, 'Ogani/blog-details.html')

def ShopGrid(request):    
    return render(request, 'Ogani/shop-grid.html')

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def MenuDetailMethod(request,pk):
    DTOTblBanner = Image.objects.filter(ImageTypeID=1)
    DTOLogo = Image.objects.filter(ImageTypeID=2)
    DTOSidebarLeft = Image.objects.filter(ImageTypeID=3)
    DTOSidebarRight = Image.objects.filter(ImageTypeID=4)
    DTOSlideShow = Image.objects.filter(ImageTypeID=5)
    DTOFooter = Image.objects.filter(ImageTypeID=6)
    DTOTopMenu = TopMenu.objects.all()
    DTOMenuDetail = MenuDetail.objects.filter(MenuID=pk)
    context = {
        'DTOMenuDetails' : DTOMenuDetail,
        'DTOTblBanners' : DTOTblBanner,
        'DTOLogos' : DTOLogo,
        'DTOSlideShows' : DTOSlideShow,
        'DTOSidebarLefts' : DTOSidebarLeft,
        'DTOSidebarRights' : DTOSidebarRight,
        'DTOFooters' : DTOFooter,
        'DTOTopMenus' : DTOTopMenu,

    }
    return render(request, 'accounts/MenuDetail.html', context)

def ContactUs(request):    
    DTOTblBanner = TblBanner.objects.all()
    context = {
        'DTOTblBanners' : DTOTblBanner
    }
    return render(request, 'accounts/ContactUS.html', context)

def AboutUs(request):    
    DTOTblBanner = TblBanner.objects.all()
    context = {
        'DTOTblBanners' : DTOTblBanner
    }
    return render(request, 'accounts/AboutUs.html', context)

def Index(request):    
    DTOTblBanner = Image.objects.filter(ImageTypeID=1)
    DTOLogo = Image.objects.filter(ImageTypeID=2)
    DTOSidebarLeft = Image.objects.filter(ImageTypeID=3)
    DTOSidebarRight = Image.objects.filter(ImageTypeID=4)
    DTOSlideShow = Image.objects.filter(ImageTypeID=5)
    DTOFooter = Image.objects.filter(ImageTypeID=6)
    DTOTopMenu = TopMenu.objects.all()
    context = {
        'DTOTblBanners' : DTOTblBanner,
        'DTOLogos' : DTOLogo,
        'DTOSlideShows' : DTOSlideShow,
        'DTOSidebarLefts' : DTOSidebarLeft,
        'DTOSidebarRights' : DTOSidebarRight,
        'DTOFooters' : DTOFooter,
        'DTOTopMenus' : DTOTopMenu,
    }
    return render(request, 'accounts/Index.html', context)

def Login(request):
    DTOTblBanner = TblBanner.objects.all()
    context = {
        'DTOTblBanners' : DTOTblBanner
    }
    return render(request, 'accounts/Login.html', context)

def Products(request):
    DTOTblBanner = TblBanner.objects.all()
    context = {
        'DTOTblBanners' : DTOTblBanner
    }
    return render(request, 'accounts/Products.html', context)


# ListCreateAPIView provides GET (list) and POST (create) actions
class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions for Category
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions for Category
class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#
def list_product_api(request):
    return render(request, 'Ogani/ListProductAPI.html')

def create_Book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publish_date = request.POST.get('published_date')
        Book.objects.create(
            titile=title,
            author=author,
            published_date=publish_date
        )
        return redirect('book_list')
    return render(request, 'Ogani/create_book.html')  # Render a form for creating a book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Ogani/book_list.html', {'books': books})  

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.titile = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'Ogani/update_book.html', {'book': book})  

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'Ogani/delete_book.html', {'book': book})