from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('products/', product_list, name='all_product'),
    path('product/create/', add_product, name='add_product'),
    path('product/edit/<str:slug>/', edit_product, name='edit_product'),
    path('product/delete/<str:slug>/', delete_product, name='delete_product'),
    path('categories/', category_list, name='all_category'),
    path('category/<int:id>/edit/', edit_category, name='edit_category'),
    path('category/<int:id>/delete/', delete_category, name='delete_category'),
    path('subcategories/', subcategory_list, name='all_subcategory'),
    path('subcategory/<int:id>/edit/', edit_subcategory, name='edit_subcategory'),
    path('subcategory/<int:id>/delete/', delete_subcategory, name='delete_subcategory'),
    path('subsubcategories/', sub_subcategory_list, name='all_subsubcategory'),
    path('subsubcategory/<int:id>/edit/', edit_sub_subcategory, name='edit_subsubcategory'),
    path('subsubcategory/<int:id>/delete/', delete_sub_subcategory, name='delete_subsubcategory'),
    path('all-orders/', view_orders, name='all_order'),
    path('order/<int:id>/', view_order_details, name='order_details'),
    path('all-customer/', view_customer, name='all_customer'),
]
