import datetime
import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.functions import ExtractYear, ExtractMonth, TruncMonth
from django.shortcuts import render, redirect

from core.models import Products, Category, SubCategory, SubSubCategory, Order, Customer, OrderItems
from django.utils import timezone

from .forms import CategoryForm, SubCategoryForm, SubSubCategoryForm, ProductForm


# from account.models import Profile


def admin_dashboard_view(request):
    total_products = Products.objects.count()
    categories = Category.objects.count()
    total_subcategories = SubCategory.objects.count()
    total_subsubcategories = SubSubCategory.objects.count()
    total_categories = categories + total_subcategories + total_subsubcategories
    orders = Order.objects.all()

    item_per_page = 6
    paginator = Paginator(orders, item_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    total_order = orders.count()
    # total_value = orders.aggregate(total_value=Sum('total_price'))['total_value']

    current_month = timezone.now().month
    current_year = timezone.now().year

    monthly_order_counts = Order.objects.annotate(year=ExtractYear('date'),
                                                  month=ExtractMonth('date')).values('year', 'month').annotate(
        total_orders=Count('id')).annotate(month_name=TruncMonth('date')).order_by('year', 'month')

    current_month_name = get_current_month_name()

    new_member_count = count_new_members()
    new_members = new_user_show()

    context = {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_order': total_order,
        'current_month': current_month,
        'current_month_name': current_month_name,
        'current_year': current_year,
        'new_member_count': new_member_count,
        'new_members': new_members,
        'monthly_order_counts': monthly_order_counts,
        'page': page
    }
    return render(request, 'dashboard.html', context)


def get_current_month_name():
    current_month = datetime.datetime.now().strftime('%B')
    return current_month


def count_new_members(days=30):
    find_date = datetime.datetime.now() - datetime.timedelta(days=days)

    new_member_count = Customer.objects.filter(date__gte=find_date).count()
    return new_member_count


def new_user_show(days=30):
    find_date = datetime.datetime.now() - datetime.timedelta(days=days)

    new_member = Customer.objects.filter(date__gte=find_date).order_by('-date')[:3]
    return new_member


def category_list(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category successfully added.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = CategoryForm()
        category = Category.objects.all()

        item_per_page = 10
        paginator = Paginator(category, item_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    context = {
        'form': form,
        'page': page,
    }

    return render(request, 'category.html', context)


def edit_category(request, id):
    if request.method == 'post' or request.method == 'POST':
        category = Category.objects.get(pk=id)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            if 'image' in request.FILES:
                category.image.delete(save=False)
                category.save()
            else:
                category.save()
            messages.success(request, 'Category successfully updated.')
            return redirect(to='all_category')
    else:
        category = Category.objects.get(pk=id)
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'edit-category.html', context)


def delete_category(request, id):
    category = Category.objects.get(pk=id)
    if category.image:
        os.remove(category.image.path)
    category.delete()
    messages.success(request, 'Category Deleted Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))


def subcategory_list(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sub-Category successfully added.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = SubCategoryForm()
        subcategory = SubCategory.objects.all()

        item_per_page = 10
        paginator = Paginator(subcategory, item_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    context = {
        'form': form,
        'page': page,
    }

    return render(request, 'subcategory.html', context)


def edit_subcategory(request, id):
    if request.method == 'post' or request.method == 'POST':
        subcategory = SubCategory.objects.get(pk=id)
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sub-Category successfully updated.')
            return redirect(to='all_subcategory')
    else:
        subcategory = SubCategory.objects.get(pk=id)
        form = SubCategoryForm(instance=subcategory)

    context = {
        'form': form,
        'category': subcategory,
    }

    return render(request, 'edit-subcategory.html', context)


def delete_subcategory(request, id):
    category = SubCategory.objects.get(pk=id)
    category.delete()
    messages.success(request, 'Sub-Category Deleted Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))


def sub_subcategory_list(request):
    if request.method == 'POST':
        form = SubSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'SubSubCategory successfully added.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = SubSubCategoryForm()
        category = SubSubCategory.objects.all()

        item_per_page = 10
        paginator = Paginator(category, item_per_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    context = {
        'form': form,
        'page': page,
    }

    return render(request, 'subsubcategory.html', context)


def edit_sub_subcategory(request, id):
    if request.method == 'post' or request.method == 'POST':
        category = SubSubCategory.objects.get(pk=id)
        form = SubSubCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'SubSubCategory successfully updated.')
            return redirect(to='all_subsubcategory')
    else:
        category = SubSubCategory.objects.get(pk=id)
        form = SubSubCategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'edit-subsubcategory.html', context)


def delete_sub_subcategory(request, id):
    category = SubSubCategory.objects.get(pk=id)
    category.delete()
    messages.success(request, 'SubSubCategory Deleted Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))


def product_list(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    item_per_page = 20
    paginator = Paginator(products, item_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'categories': categories,

    }

    return render(request, 'products.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Product successfully added.')
        return redirect('all_product')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'add-product.html', context)


def edit_product(request, slug):
    if request.method == 'POST':
        product = Products.objects.get(slug=slug)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        messages.success(request, 'Product successfully updated.')
        return redirect(to='all_product')
    else:
        product = Products.objects.get(slug=slug)
        form = ProductForm(instance=product)

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'edit-product.html', context)


def delete_product(request, slug):
    product = Products.objects.get(slug=slug)
    if product.image:
        os.remove(product.image.path)
        os.remove(product.brand.path)
        os.remove(product.pdsliderimg1.path)
        os.remove(product.pdsliderimg2.path)
        os.remove(product.pdsliderimg3.path)

    product.delete()
    messages.success(request, 'Product Deleted Successfully.')
    return redirect(request.META.get('HTTP_REFERER'))


def view_orders(request):
    orders = Order.objects.all().order_by('-date')

    item_per_page = 10
    paginator = Paginator(orders, item_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'all_orders.html', {'page': page})


def view_order_details(request, id):
    order = Order.objects.get(pk=id)

    order_item = OrderItems.objects.filter(order=order)

    context = {
        'order': order,
        'order_item': order_item
    }

    return render(request, 'order_detail.html', context)


def view_customer(request):
    customer = Customer.objects.all().order_by('date')

    context = {
        'customer': customer
    }

    return render(request, 'customer.html', context)
