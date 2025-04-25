from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


STATUS = (
        ('in', 'In Stock'),
        ('out', 'Out of Stock'),
    )


class Category(models.Model):
    name = models.CharField(max_length=500)
    category_img = models.ImageField(upload_to="Category Image", null=True, blank=True)
    filtername = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.name = self.name.strip()
        self.filtername = self.name.replace(' ', '_')
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    filtername = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.name = self.name.strip()
        self.filtername = self.name.replace(' ', '_')
        super().save(*args, **kwargs)


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    filtername = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.name = self.name.strip()
        self.filtername = self.name.replace(' ', '_')
        super().save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ImageField(upload_to="Brand Image", default="brands/category/1.png")
    sku = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    stock_status = models.CharField(choices=STATUS, max_length=100, null=True, blank=True, default="In Stock")
    review = models.PositiveIntegerField(null=True, blank=True, default=0)
    sort_description = RichTextField(null=True, blank=True)
    # sort_description = models.TextField()
    slug = AutoSlugField(populate_from="name", null=True, unique=True)
    description = RichTextUploadingField(null=True, blank=True)
    # description = models.TextField()
    image = models.ImageField(upload_to="Product Image")
    pdsliderimg1 = models.ImageField(upload_to="Slider Image", blank=True, null=True)
    pdsliderimg2 = models.ImageField(upload_to="Slider Image", blank=True, null=True)
    pdsliderimg3 = models.ImageField(upload_to="Slider Image", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class PopularDepartMents(models.Model):
    Department = (
        ('NEWARRIVALS', 'NEWARRIVALS'),
        ('BESTSELLER', 'BESTSELLER'),
        ('MOSTPOPULAR', 'MOSTPOPULAR'),
        ('FEATURED', 'FEATURED'),
    )

    department = models.CharField(choices=Department, max_length=100)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.department


class Cart(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def line_total(self):
        return self.quantity * self.product.price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Customer(models.Model):
    objects = None
    country = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Order(models.Model):
    objects = None
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=100, default="pending")
    pymentSystem = models.CharField(max_length=100, default="Cash On Delivery")
    total_order = models.PositiveIntegerField(blank=True, null=True)
    ordernote = models.TextField()

    def __str__(self):
        return self.customer.first_name


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def order_subtotal(self):
        return self.quantity * self.product.price


class ContactSettings(models.Model):
    name = models.CharField(max_length=20)
    comment = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=400)
    fax = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.email}"


class Contact_question(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class FAQ(models.Model):
    name = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FAQQuestion(models.Model):
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class FAQSettings(models.Model):
    name = models.CharField(max_length=26)
    comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
