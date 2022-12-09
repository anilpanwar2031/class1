from django.contrib import admin
from .models import (Quotation, Section, Product, Subsection, QuotationItem)
from import_export.admin import ImportExportModelAdmin


@admin.register(Quotation)
class QuotationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quot_no', 'name', 'quot_status']


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quotation', "product_list"]


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'quantity', 'selling_price']


@admin.register(Subsection)
class SubsectionectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section', "product_list"]


# @admin.register(Client)
# class ClientModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'surname']
#
#
@admin.register(QuotationItem)
class QuotationItemModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quotation', 'version']


