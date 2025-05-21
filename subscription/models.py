from django.db import models

# Create your models here.



class User(AbstractUser):
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    max_nb_seats = models.IntegerField()
    max_selfies_per_day = models.IntegerField()

class Subscription(models.Model):
    PERIOD_CHOICES = [
        ('month', 'Month'),
        ('year', 'Year'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    started_at = models.DateField(auto_now_add=True)
    nb_of_days = models.IntegerField()
    periodity = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    is_renewable = models.BooleanField(default=True)

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    transction_date = models.DateTimeField(auto_now_add=True)
    charge_id = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Price(models.Model):
    CURRENCY_CHOICES = [
        ('CAD', 'CAD'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]
    COUNTRY_CHOICES = [
        ('Canada', 'Canada'),
        ('Usa', 'Usa'),
        ('Europe', 'Europe'),
    ]
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    country = models.CharField(max_length=40, choices=COUNTRY_CHOICES)