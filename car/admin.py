from django.contrib import admin
from .models import Car, CarImage
# Register your models here.




class GalleryInline(admin.TabularInline):
    fk_name = 'car'
    model = CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]

# admin.site.register(CarImage)



# class GalleryInline(admin.TabularInline):
#     fk_name = 'car'
#     model = CarImage
#
# admin.site.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     inlines = [GalleryInline,]
