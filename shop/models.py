from django.db import models
import uuid
# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.conf import settings
from django.conf import settings
import random 
import string

class ShopUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class ShopUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ShopUserManager()

    USERNAME_FIELD = "email"
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin





class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self) -> str:
        return self.name
    



class Product(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='shop/')
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    size = models.CharField(max_length=24,default='Small')
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)
     
    def __str__(self) -> str:
        return self.name
    
    

    class Meta:
        ordering = ['created_at']


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICE =[
        ('Pending','pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancled','Cancelled')
    ]
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orders')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='orders')
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,default='pending',choices=STATUS_CHOICE)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return self.status
    
    class Meta:
        ordering =['ordered_date','status']



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sub_total = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return self.quantity



class ShippingAddress(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='shippingaddress')
    address = models.TextField()
    item = models.OneToOneField(Order,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.address
    


class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reviews')
    comments = models.TextField()
    rating = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comments
    

    class Meta:
        ordering = ['date_added']










