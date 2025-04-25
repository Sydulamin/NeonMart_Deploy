from django import forms
from django.forms import ModelForm

from core.models import Category, SubCategory, SubSubCategory, Products, STATUS


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Category Name', 'style': 'background:transparent'}),
            'category_img': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'})
        }


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Category Name', 'style': 'background:transparent'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
        }


class SubSubCategoryForm(ModelForm):
    class Meta:
        model = SubSubCategory
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Category Name', 'style': 'background:transparent'}),
            'subcategory': forms.Select(attrs={'class': 'form-select', 'style': 'background:transparent'})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['review', 'slug']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Product Name', 'style': 'background:transparent'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'sub_sub_category': forms.Select(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'brand': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'sku': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Product SKU', 'style': 'background:transparent'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'style': 'background:transparent'}),
            'stock_status': forms.Select(choices=STATUS, attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'sort_description': forms.TextInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'pdsliderimg1': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'pdsliderimg2': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
            'pdsliderimg3': forms.FileInput(attrs={'class': 'form-control', 'style': 'background:transparent'}),
        }
