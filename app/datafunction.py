from .models import Quotation, Product, Section, Subsection



def sectionSubProduct(sections):
    data = []
    gt = 0
    for s in sections:
        sprodts, sectiontotal, sitems = [], 0, 0
        section = {'id': s.id, 'name': s.name, 'quotation': s.quotation.id}

        pds = Section.objects.filter(id=s.id).values('product')

        pn = 0
        for p in pds:
            pn = pn + 1
            prod = Product.objects.get(id=p["product"])
            pdict = {'id': prod.id, 'name': prod.name, 'description': prod.description, 'quantity': prod.quantity,
                     'selling_price': prod.selling_price}
            sectiontotal = sectiontotal + prod.selling_price
            sprodts.append(pdict)
        print("SEction pn", pn)
        sitems = sitems + pn
        section['sprodts'] = sprodts

        subsectns = []
        subs = Subsection.objects.filter(section=s.id)
        for sub in subs:
            subprodts, subtotal, subitems = [], 0, 0
            subsection = {'id': sub.id, 'name': sub.name}

            pds = Subsection.objects.filter(id=sub.id).values('product')

            pn = 0
            for p in pds:
                pn = pn + 1
                prod = Product.objects.get(id=p["product"])
                pdict = {'id': prod.id, 'name': prod.name, 'description': prod.description, 'quantity': prod.quantity,
                         'selling_price': prod.selling_price}

                subtotal = subtotal + prod.selling_price
                sectiontotal = sectiontotal + prod.selling_price
                subprodts.append(pdict)
            sitems = sitems + pn
            subitems = subitems + pn
            subsection['subtotal'] = subtotal
            subsection['subprodts'] = subprodts
            subsection['subitems'] = subitems
            subsectns.append(subsection)

        section['subsectns'] = subsectns
        section['sectiontotal'] = sectiontotal
        section['sitems'] = sitems
        gt = gt + sectiontotal
        data.append(section)
    data1 = [data, gt]
    return data1




# def grandtotal(sections):
#     gt = 0
#     print("No of Sections : ", len(sections))
#     for s in sections:
#         print("Section id , Name ", s.id, " ", s.name)
#         try:
#             pds = Section.objects.filter(id=s.id).values('product__selling_price')
#             for pd in pds:
#                 print("Price : ", pd["product__selling_price"])
#                 gt = gt + pd["product__selling_price"]
#         except:
#             pass
#     print("Section Grant Total : ", gt)
#
#     for s in sections:
#         try:
#             subs = Subsection.objects.filter(section=s.id)
#             print("No of Subsections : ", len(subs))
#             for sub in subs:
#                 print("Sub Section id , Name ", sub.id, " ", sub.name)
#                 try:
#                     pds = Subsection.objects.filter(id=sub.id).values('product__selling_price')
#                     for pd in pds:
#                         print("Price : ", pd["product__selling_price"])
#                         gt = gt + pd["product__selling_price"]
#                 except:
#                     pass
#         except:
#             pass
#     print("Grand Total : ", gt)
#     return gt

