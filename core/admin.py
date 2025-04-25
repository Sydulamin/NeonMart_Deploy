from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('filtername',)

    def save_model(self, request, obj, form, change):
        obj.filtername = obj.name.lower().strip()
        super().save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    exclude = ('filtername',)

    def save_model(self, request, obj, form, change):
        obj.filtername = obj.name.lower().strip()
        super().save_model(request, obj, form, change)


admin.site.register(SubCategory, SubCategoryAdmin)


class SubSubCategoryAdmin(admin.ModelAdmin):
    exclude = ('filtername',)

    def save_model(self, request, obj, form, change):
        obj.filtername = obj.name.lower().strip()
        super().save_model(request, obj, form, change)


admin.site.register(SubSubCategory, SubSubCategoryAdmin)

admin.site.register([Products, PopularDepartMents])
admin.site.register([Cart, Wishlist])
admin.site.register([Customer, Order, OrderItems])
admin.site.register(ContactSettings)
admin.site.register(Contact)
admin.site.register(Contact_question)


class FAQQuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


admin.site.register(FAQQuestion, FAQQuestionAdmin)
admin.site.register(FAQ)
admin.site.register(FAQSettings)
