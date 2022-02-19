import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='customer/avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

class Courier(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  lat = models.FloatField(default=0)
  lng = models.FloatField(default=0)
  #paypal_email = models.EmailField(max_length=255, blank=True)
  fcm_token = models.TextField(blank=True)

  def __str__(self):
    return self.user.get_full_name()

class Category(models.Model):
  slug = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Job(models.Model):
  SMALL_SIZE = "small"
  MEDIUM_SIZE = "medium"
  LARGE_SIZE = "large"
  SIZES = (
    (SMALL_SIZE, 'Small'),
    (MEDIUM_SIZE, 'Medium'),
    (LARGE_SIZE, 'Large'),
  )

  Cash_on_Pickup = "Cash on Pickup"
  Cash_on_Delivery = "Cash on Delivery"
  pmethods = (
    (Cash_on_Pickup, 'Cash on Pickup'),
    (Cash_on_Delivery, 'Cash on Delivery'),
  )

  CREATING_STATUS = 'creating'
  PROCESSING_STATUS = 'processing'
  PICKING_STATUS = 'picking'
  DELIVERING_STATUS = 'delivering'
  COMPLETED_STATUS = 'completed'
  CANCELED_STATUS = 'canceled'
  STATUSES = (
    (CREATING_STATUS, 'Creating'),
    (PROCESSING_STATUS, 'Processing'),
    (PICKING_STATUS, 'Picking'),
    (DELIVERING_STATUS, 'Delivering'),
    (COMPLETED_STATUS, 'Completed'),
    (CANCELED_STATUS, 'Canceled'),
  )

  # Step 1
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  courier = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  size = models.CharField(max_length=20, choices=SIZES, default=MEDIUM_SIZE)
  weight = models.FloatField(default=1)
  payment_method = models.CharField(max_length=30, choices=pmethods, default=MEDIUM_SIZE)
  photo = models.ImageField(upload_to='job/photos/')
  status = models.CharField(max_length=20, choices=STATUSES, default=CREATING_STATUS)
  created_at = models.DateTimeField(default=timezone.now)
# Pickup details
  pickup_address=models.CharField(max_length=255, blank=True)
  pickup_lat=models.FloatField(default=0)
  pickup_lng=models.FloatField(default=0)
  pickup_name=models.CharField(max_length=255, blank=True)
  pickup_phone=models.CharField(max_length=15, blank=True)

  #Delivery Details
  delivery_address=models.CharField(max_length=255, blank=True)
  delivery_lat=models.FloatField(default=0)
  delivery_lng=models.FloatField(default=0)
  delivery_name=models.CharField(max_length=255, blank=True)
  delivery_phone=models.CharField(max_length=15, blank=True)

  #Payment
  #duration = models.IntegerField(default=0)
  distance = models.FloatField(default=0)
  price = models.FloatField(default=0)

    # Extra info
  pickup_photo = models.ImageField(upload_to='job/pickup_photos/', null=True, blank=True)
  pickedup_at = models.DateTimeField(null=True, blank=True)

  delivery_photo = models.ImageField(upload_to='job/delivery_photos/', null=True, blank=True)
  delivered_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
 return self.name 

class Transaction(models.Model):
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  amount = models.FloatField(default=0)
  #status = models.CharField(max_length=20, choices=STATUSES, default=IN_STATUS)
  created_at = models.DateTimeField(default=timezone.now)

  def __obj__(self):
    return self.job