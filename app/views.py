from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product, Section, Subsection
# , Product, Quotation_item, Client, Section
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime
from .models import quotationstatus
from .datafunction import sectionSubProduct


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
    quot = Quotation.objects.get(id=pk)
    # print("Quotation ", type(quot))
    sections = Section.objects.filter(quotation=pk)
    prods = []
    gt = 0; data = []
    data1 = sectionSubProduct(sections)
    data, gt = data1[0], data1[1]

    #                    s.prods[0].name
    # print("DATAAA", data[0]['subsectns'][0]["name"])
    context = {'data': data, 'products': products, 'quot': quot, 'grandtotal': gt, "quotationstatus": quotationstatus}
    return render(request, "quotationdetail.html", context)


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods": prods})


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
        print("Data = ", data)
        return JsonResponse(data, safe=False)
