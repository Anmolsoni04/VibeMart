from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=500, default='')
    items_json = models.CharField(max_length=1000)
    amount = models.IntegerField(default=0)
    Email = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    Address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, default="blank")
    razorpay_order_id = models.CharField(max_length=100, default="blank")
    payment_signature = models.CharField(max_length=100, default="blank")
    payment_id = models.CharField(max_length=100, default="blank")
    payment_done_amount = models.CharField(max_length=100, default="blank")

    def __str__(self):
        return self.Email

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
