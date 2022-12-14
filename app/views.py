from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product, Section, Subsection
# , Product, Quotation_item, Client, Section
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime
from .models import quotationstatus
from .datafunction import sectionSubProduct
from django.core.paginator import Paginator
import random, string
import pandas as pd

import os

from pathlib import Path


def export_data(request):
    prods = Product.objects.all()
    data = []
    for p in prods:
        data.append({'Name': p.name, 'Description': p.description, 'Quatantity':p.quantity, 'Price': p.selling_price})
    pd.DataFrame(data).to_excel('products.xlsx')
    # print(data)
    return redirect('products')



def index(request):
    return render(request, 'index.html')


def dashboard(request):
    quots = Quotation.objects.all().count()
    products = Product.objects.all().count()
    users = User.objects.all().count()
    active = 'dashboard'
    return render(request, "dashboard.html", {"quots": quots, "products": products, "users": users, "active": active})


def quotation(request):
    quots = Quotation.objects.all()
    return render(request, "quotation.html", {"quots": quots})


def quotdetail(request, pk):
    print("\n")
    print("\n")
    print("pk ", pk)

    products = Product.objects.all()
    p = Paginator(products, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    quot = Quotation.objects.get(id=pk)
    # print("Quotation ", type(quot))
    sections = Section.objects.filter(quotation=pk)
    prods = []
    gt = 0; data = []
    data1 = sectionSubProduct(sections)
    data, gt = data1[0], data1[1]

    context = {'data': data, 'products': products, 'quot': quot, 'grandtotal': gt,
               "quotationstatus": quotationstatus,'page_obj': page_obj}
    return render(request, "quotationdetail.html", context)


def products(request):
    prods = Product.objects.all()
    p = Paginator(prods, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request, "product.html", {"page_obj": page_obj})


def newquote(request):
    rnum = random.randint(10000, 100000)
    rchar = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    print("NUM", rnum)
    print("CHAR", rchar)


    qnumber = rchar+'-'+str(rnum)+'.1'
    print(qnumber)
    products = Product.objects.all()
    p = Paginator(products, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {'page_obj': page_obj, "quotationstatus": quotationstatus, 'qnumber':qnumber, 'rnum': rnum, 'rchar': rchar}

    return render(request, "newquote.html", context)


def savequote(request):

    return render(request, 'index.html')



def deletesp(request, qid, sid, pid):
    print("section quote, section , prod", sid, pid)
    sec = Section.objects.get(id=sid)
    sec.product.remove(pid)
    return redirect('quotdetail', qid)


def deletesubp(request, qid, subid, pid):
    print("subsection, prod", subid, pid)
    sub = Subsection.objects.get(id=subid)
    pd = sub.product.all()

    print("PROOD", pd)
    sub.product.remove(pid)
    return redirect('quotdetail', qid)



def qsearch(request):
    if request.method == 'POST':
        search = request.POST['search'].lower()
        print("Search = = ", search)

        queryset = Quotation.objects.filter(Q(quot_no__icontains=search) | Q(name__icontains=search) | Q(quot_status__icontains=search) | Q(market_seg__icontains=search))
        data = [{'id': d.id, 'quot_no': d.quot_no, 'name': d.name, 'quot_status': d.get_quot_status_display(), 'market_seg': d.market_seg,
                 'created_at': d.created_at.strftime("%b %d,%Y") + " | " + d.created_at.strftime("%H:%M %p").lower(), 'created_by': d.created_by.email} for d in queryset]

        for d in queryset:
            print("datetime", d.created_at.strftime("%b %d,%Y") + " | " + d.created_at.strftime("%H:%M %p").lower())
        # print("Data1 = ", data)
        return JsonResponse(data, safe=False)


def psearch(request):
    if request.method == 'POST':
        search = request.POST['search'].lower()
        print("Search = = ", search)

        queryset = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search)).values()
        data = list(queryset)
        # print("Data = ", data)
        return JsonResponse(data, safe=False)
