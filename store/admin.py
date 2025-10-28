from django.contrib import admin,messages
from django.db.models import Count, QuerySet
from django.utils.html import format_html,urlencode
from django.urls import reverse
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        ]
    
    def queryset(self, request, queryset:QuerySet):
        if self.value() == '<10':
           return queryset.filter(inventory__lt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    search_fields = ['order']
    actions= ['clear_inventory']
    list_display = ['title','unit_price','inventory_status','collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = [ 'collection' ]
    # 17 queries to7 queries

    def collection_title(self,product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory <10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products has been updated',
            messages.INFO
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','membership','order_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering =  ['first_name']
    search_fields=['first_name__istartswith']

    def order_count(self,order):
        return order.order_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count = Count('order')
        )
    
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    autocomplete_fields = ['product']
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']
    ordering =  ['id']
    inlines = [OrderItemInline]
    list_per_page = 10
    autocomplete_fields = ['customer']

@admin.register(models.Collection)
class CollectionAmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    search_fields = ['title']
     
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = (
            reverse('admin:store_product_changelist')
            +'?'
            +urlencode({
              'collection__id':str(collection.id)
            }))
        return format_html('<a href={}>{}</a>',url,collection.products_count)
         
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )
