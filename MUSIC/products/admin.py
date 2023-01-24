from django.contrib import admin
from products.models import products

class productsadmin(admin.ModelAdmin):
    list_display=('products_NAME','category_NAME','Subcategory','price','price','publish_date','publish_image')
admin.site.register(products,productsadmin)

# Register your models here.
