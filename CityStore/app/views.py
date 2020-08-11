from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm, Productform
from .models import ShopDetail,Product
# from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            mobile=form.cleaned_data.get('mobile')
            time=form.cleaned_data.get('time')
            shopname=form.cleaned_data.get('shopname')
            address=form.cleaned_data.get('address')
            username=form.cleaned_data.get('username')
            holiday=form.cleaned_data.get('holiday')
            gstno=form.cleaned_data.get('gstno')
            shopowner=form.cleaned_data.get('shopowner')
            myshopname=form.cleaned_data.get('myshopname')
            form.save()

            ShopDetail(user=User.objects.filter(username=username).first(),mobile=mobile,gstno=gstno,time=time,shopname=shopname,address=address,shopowner=shopowner,holiday=holiday).save()
    else:
        form=UserRegistrationForm()
    par={
        'form':form,
    }
    return render(request,'signup.html',par)
@login_required
def addproduct(request):
    if request.method == "POST":
        form=Productform(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            description=form.cleaned_data.get('description')
            price=form.cleaned_data.get('price')
            address=request.user.shopdetail.address
            image=form.cleaned_data.get('image')
            shopname=request.user.shopdetail.shopname

            # form.save()
            Product(name=name,address=address,price=price,description=description,image=image,shopname=shopname).save()
    else:
        form=Productform()
    par={
        'form':form
    }
    return render(request,'addproduct.html',par)


def search(request):
    qur=request.GET.get('search').lower()
    qur2=request.GET.get('search2').lower()
    result1=[item for item in Product.objects.all() if qur in item.name.lower() ]
    result2=[item for item in Product.objects.all() if qur2 in item.address.lower()]
    result= [value for value in result1 if value in result2]
    return render(request,'search.html',{'results':result})

@login_required()
def myproduct(request):
    return render(request,'myproduct.html')


@login_required()
def myproductsearch(request):
    qur=request.user.shopdetail.shopname.lower()
    result=[item for item in Product.objects.all() if qur in item.shopname.lower()]
    return render(request,'myproductsearch.html',{'results':result})

def delete_post(request,post_id=None):
    post_to_delete=Product.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponse("<h1>Deleted</h1>")