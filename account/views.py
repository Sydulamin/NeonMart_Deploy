from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import *


def login_(request):
    if not request.user.is_authenticated:
        msg = ""
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active and user.is_staff and user.is_superuser:
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    login(request, user)
                    return redirect('HOME')
            else:
                msg = "something wrong!! please try again."

        context = {
            'msg': msg
        }
        return render(request, "account/login.html", context)
    else:
        return redirect('HOME')


def registration(request):
    if not request.user.is_authenticated:
        msg = ""
        if request.method == "POST":
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_valid_check = User.objects.filter(username=username).exists()
            if user_valid_check:
                msg = 'User name or Email already exist!!'
                return redirect("login")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password)
                user.save()
                login(request, user)
                return redirect("login")
        context = {
            'msg': msg
        }
        return render(request, "account/login.html", context)
    else:
        return redirect('my-account')


# def my_account(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user)
#         orders = Order.objects.filter(user=request.user)
#         customer = Customer.objects.filter(user=request.user).last()
#         context ={
#             'navbar':'my_account',
#             'cart':cart,
#             'orders':orders,
#             'customer':customer
#         }
#         return render(request,"account/my_account.html",context)
#     else:
#         return redirect("login")


def my_account(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user)
        orders = Order.objects.filter(user=user)
        customer, created = Customer.objects.get_or_create(user=user)

        categories = Category.objects.all()
        category_subcategories = {category: SubCategory.objects.filter(category=category) for category in
                                  categories}
        subcategory_subsubcategories = {subcategory: SubSubCategory.objects.filter(subcategory=subcategory) for
                                        subcategory in SubCategory.objects.all()}

        if request.method == 'POST':
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            mail = request.POST.get('email_1')
            customer.first_name = fname
            customer.last_name = lname
            customer.email = mail
            customer.save()

            old_password = request.POST.get('cur_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('conf_password')

            if authenticate(username=user.username, password=old_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    logout(request)
                    return redirect("HOME")

        context = {
            'navbar': 'my_account',
            'cart': cart,
            'orders': orders,
            'customer': customer,
            'categories': categories,
            'category_subcategories': category_subcategories,
            'subcategory_subsubcategories': subcategory_subsubcategories,
        }
        return render(request, "account/my_account.html", context)
    else:
        return redirect("login")


def signout(request):
    logout(request)
    return redirect("HOME")
