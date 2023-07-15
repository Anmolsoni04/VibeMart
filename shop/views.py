import email
from builtins import zip

from django.shortcuts import render, redirect
from django.contrib import messages
import razorpay
from django.conf import settings


from scipy.spatial._ckdtree import ordered_pairs
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'


def index(request):
    allProducts = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    products = Product.objects.all()
    # print(products)
    for category in categories:
        prod = Product.objects.filter(category=category)
        n = len(products)
        no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, range(1, no_of_slides), no_of_slides])
    params = {'allProducts': allProducts}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    #return true only if query matches the item
    if query.lower() in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search','')
    allProducts = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    products = Product.objects.all()
    # print(products)
    for category in categories:
        prodtemp = Product.objects.filter(category=category)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(products)
        no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allProducts.append([prod, range(1, no_of_slides), no_of_slides])
    params = {'allProducts': allProducts}
    # if len(allProducts) == 0 or len(query)<4:
    if len(allProducts) == 0:
        params = {'msg':"Please enter relevant search query"}
    return render(request, 'shop/search.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "We have recieved ur contact details")
        return redirect("/shop/contact/")

    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        print("Entered")
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        print(email, orderId)
        try:
            order = Orders.objects.filter(razorpay_order_id =orderId, Email=email).first()
            if order:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order.items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            print(e)
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def productView(request, myid):
    # fetch the product using id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        amount = int(request.POST.get('amount', ''))
        Email = request.POST.get('email', '')
        Address = request.POST.get('address1', '')
        Address_line_2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone_number = request.POST.get('phone', '')
        test_key = settings.TEST_KEY
        key_secret = settings.KEY_SECRET
        client = razorpay.Client(
            auth=(test_key, key_secret)
        )
        payment = client.order.create({'amount': amount*100, 'currency': 'INR',
                                       'payment_capture': '1'})
        order = Orders(
            name=name,
            items_json=items_json,
            Email=Email,
            Address=Address,
            Address_line_2=Address_line_2,
            city=city,
            state=state,
            zip=zip,
            phone_number=phone_number,
            amount=amount,
            razorpay_order_id=payment['id']
        )
        order.save()
        params = {
            'name':name,
            'email':Email,
            'address':Address,
            'add2':Address_line_2,
            'city':city,
            'state':state,
            'zip':zip,
            'phno':phone_number,
            'payment':payment,
            'key':test_key
        }
        return render(request, 'shop/checkout.html', params)
    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        order_id = request.POST.get('orderID')
        amount = request.POST.get('amount')
        payment_signature = request.POST.get('payment_signature')
        payment_id = request.POST.get('payment_id')
        order = Orders.objects.filter(razorpay_order_id=order_id).first()
        if order:
            order.payment_signature = payment_signature
            order.payment_id = payment_id
            order.payment_done_amount = amount
            order.save()
            return render(request, "shop/success.html")
