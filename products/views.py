from django.shortcuts import render, get_object_or_404
from.models import Product,Services,Banner,Sidebanner,Discount
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    dic_product=Product.objects.all()[:12] 
    dic_services=Services.objects.all()
    dic_banner=Banner.objects.all()
    dic_side_banner=Sidebanner.objects.all()
    dic_discount=Discount.objects.all()[:4]



    return render(request,'index.html',{'items':dic_product,'serv':dic_services,'ban':dic_banner,'side_ban':dic_side_banner,'discount':dic_discount})


def product(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'product.html', {'page_obj': page_obj})


def product_details(request):
    return render(request,'product_details.html')

def category(request):
    category_list = Product.objects.all()
    paginator = Paginator(category_list, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'category.html', {'page_obj': page_obj})


def cart(request):
    return render(request,'cart.html')

def account(request):
    return render(request,'account.html')