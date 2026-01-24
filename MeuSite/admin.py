from django.contrib import admin
from .models import Lead, Sales_Dashboard

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')



@admin.register(Sales_Dashboard)
class SalesDashboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'lead', 'service_interested', 'budget', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'lead__name', 'service_interested', 'status')
    list_filter = ('status', 'created_at', 'updated_at')

