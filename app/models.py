from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

quotationstatus = (
    ("no", "No Status"),
    ("scnf", "Spec Confirmed"),
    ("act", "Active"),
    ("hold", "On-hold"),
    ("ocnf", "Order Confirmed"),
)


class Quotation(models.Model):
    quot_no = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    quot_status = models.CharField(max_length=5, choices=quotationstatus, default="no")
    market_seg = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # quot_total = models.IntegerField()

    def __str__(self):
        # return self.user.username
        return str(self.id)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    selling_price = models.FloatField()

#
#     # prodtype = models.CharField(max_length=100)
#     # unitsale = models.CharField(max_length=100)
#     # unitsale2 = models.CharField(max_length=100)
#     # factor_1 = models.CharField(max_length=100)
#     # is_flooring_product = models.BooleanField(default=False)
#     # m2_price = models.BooleanField(default=False)
#     # active_field = models.BooleanField(default=False)
#     # product_image = models.ImageField(upload_to='productimg')
#
    def __str__(self):
        return str(self.id)


class Section(models.Model):
    name = models.CharField(max_length=100)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def product_list(self):
        return ",".join([str(p) for p in self.product.all()])


class Subsection(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def product_list(self):
        return ",".join([str(p) for p in self.product.all()])


class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    version = models.IntegerField(default=1, null=True, blank=True)


# # class Client(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     # telephone = models.CharField(max_length=200)
#     # mobile = models.CharField(max_length=200)
#     email = models.EmailField(max_length=254)
#     quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
# #     # address = models.CharField(max_length=200)
# #     # notes = models.CharField(max_length=200)
# #     # method = models.CharField(max_length=200)
# #     # city = models.CharField(max_length=50)
# #     # country = models.CharField(max_length=100)
# #     # suburb = models.CharField(max_length=100)
# #     # province = models.CharField(max_length=100)
# #     # postalcode = models.IntegerField()
# #     # address1 = models.CharField(max_length=100)
# #     # address2 = models.CharField(max_length=100)
# #     # notes1= models.CharField(max_length=100)
# #
#     def __str__(self):
#         # return self.user.username
#         return str(self.id)


