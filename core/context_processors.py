from .models import *


def cate(request):
    categories = Category.objects.all()
    category_subcategories = {category: SubCategory.objects.filter(category=category) for category in categories}
    subcategory_subsubcategories = {subcategory: SubSubCategory.objects.filter(subcategory=subcategory) for subcategory
                                    in SubCategory.objects.all()}
    return {
        'categories': categories,
        'category_subcategories': category_subcategories,
        'subcategory_subsubcategories': subcategory_subsubcategories,
    }
