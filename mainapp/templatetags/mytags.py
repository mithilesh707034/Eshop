from django import template
from mainapp.models import Checkout,CheckoutProducts,Product
register = template.Library()

@register.filter(name='checkoutProducts')
def checkoutProducts(checkoutid):
    checkout=Checkout.objects.get(id=checkoutid)
    cp=CheckoutProducts.objects.filter(checkout=checkout)
    c=[]
    for item in cp:
        x={'name':item.p.name,'maincategory':item.p.Maincategory,'subcategory':item.p.Subcategory,'brand':item.p.Brand,'color':item.p.color,'price':item.p.finalprice,'qty':item.qty,'total':item.total,'pic':item.p.pic1.url}
        c.append(x)
    return c

@register.filter(name='paymentStatus')
def paymentStatus(op):
   if op==0:
    return "Pending"
   else:
    return "Done"
    
@register.filter(name='paymentMode')
def paymentMode(op):
   if op==0:
    return "COD"
   else:
    return "Net Banking" 

@register.filter(name='orderStatus')
def orderStatus(op):
   if op==0:
    return "Order Placed"
   elif op==1:
    return "Not Packed"
   elif op==2:
    return "Packed" 
   elif op==3:
    return "Ready to Ship"
   elif op==4:
    return "Shiped"
   elif op==5:
    return "Out for Delivered"
   elif op==6:
    return "Delevered"
   elif op==7:
    return "Cancelled"
     