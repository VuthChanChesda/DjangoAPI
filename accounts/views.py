from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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