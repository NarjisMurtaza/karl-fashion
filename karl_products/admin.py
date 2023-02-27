from django.contrib import admin
from .models import product
from .models import category
# for reviews\
from .models import Review
from .models import Cart


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "color")}
admin.site.register(product,ProductAdmin)
admin.site.register(category)
admin.site.register(Review)
admin.site.register(Cart)




