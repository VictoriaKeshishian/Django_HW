from django.contrib import admin
from .models import User, Product, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'date_registration')
    search_fields = ('name', 'email', 'number', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'amount', 'date_add_product')
    list_filter = ('date_add_product',)
    search_fields = ('name', 'description')
    readonly_fields = ('date_add_product',)
    readonly_fields = ['date_add_product', 'rating']
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
        ('Подробности', {
            'fields': ('description', 'price', 'amount'),
            'classes': ('collapse',),
        }),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_add_product'],
            }
        ),
    )

    @admin.action(description="Сбросить количество в ноль")
    def reset_quantity(self, request, queryset):
        queryset.update(amount=0)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'total_price')
    list_filter = ('date_ordered',)
    search_fields = ('customer__name',)
