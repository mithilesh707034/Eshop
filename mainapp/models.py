from django.db import models

class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    Maincategory=models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    Subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE) 
    color=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    stock=models.CharField(max_length=20,default="In Stock" ,null=True,blank=True)
    description=models.TextField()
    baseprice=models.IntegerField()
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalprice=models.IntegerField()
    pic1=models.ImageField(upload_to="uploads" ,default='',null=True,blank=True)
    pic2=models.ImageField(upload_to="uploads" ,default='',null=True,blank=True)
    pic3=models.ImageField(upload_to="uploads" ,default='',null=True,blank=True)
    pic=models.ImageField(upload_to="uploads" ,default='',null=True,blank=True)

    #on_delete=models.CASCADE : When You want to delete all product of Miancategory as well as Product
    #on_delete=PROTECT: When You want to Keep  atleat one product of Miancategory which refer the product foregin key

    #on_delete=SET_DEFAULT: When You want to delete all product and set some default value in Miancategory which refer the product foregin key

    #on_delete=models.DO_NOTHING: When you want do nothing
    def __str__(self):
        return self.name

class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=15)
    addressline1=models.CharField(max_length=150)
    addressline2=models.CharField(max_length=150)
    addressline3=models.CharField(max_length=150)
    pin=models.CharField(max_length=15)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=15)
    pic=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    otp=models.IntegerField(default=-875945)

    def __str__(self):
        return str(self.id)+"  "+self.username

class Wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+' '+ self.user.username +' '+ self.product.name

status=((0,"Order Placed"),(1,"Not Packed"),(2,"Packed"),(3,"Ready to Ship"),(4,"Shiped"),(5,"Out for Delivered"),(6,"Delevered"),(7,"Cancelled"))   
payment=((0,"Pending"),(1,"Done"))
mode=((0,"COD"),(1,"Net Banking"))
class Checkout(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Buyer, on_delete=models.CASCADE)
    total=models.IntegerField()
    shipping=models.IntegerField()
    final=models.IntegerField()
    rppid=models.CharField(max_length=30,blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    paymentmode=models.IntegerField(choices=mode,default=0)
    paymentstatus=models.IntegerField(choices=payment,default=0)
    orderstatus=models.IntegerField(choices=status,default=0)

    def __str__(self):
        return str(self.id)+" " + self.user.username

class CheckoutProducts(models.Model):
    id=models.AutoField(primary_key=True)
    checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE)
    p=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    total=models.IntegerField()

    def __str__(self):
        return str(self.id)+' '+str(self.checkout.user.username)

contactstatus=((0,"Active"),(1,"Done"))
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    status=models.IntegerField(choices=contactstatus,default=0)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+' '+self.name+ ' '+(self.subject)