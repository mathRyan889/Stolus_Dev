import openpyxl
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import Lead, Services, Sales_Dashboard

# Função de Ação para Exportar para Excel
def exportar_leads_excel(modeladmin, request, queryset):
    # Cria o workbook e a planilha ativa
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Leads"

    # Define o cabeçalho
    columns = ['Nome', 'Email', 'Whatsapp', 'Criado em']
    sheet.append(columns)

    # Adiciona os dados do queryset
    for lead in queryset:
        sheet.append([
            lead.name,
            lead.email,
            lead.phone,
            lead.created_at.strftime('%d/%m/%Y %H:%M') if lead.created_at else ''
        ])

    # Prepara a resposta HTTP
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=leads_exportados.xlsx'
    
    workbook.save(response)
    return response

exportar_leads_excel.short_description = "Exportar Leads Selecionados para Excel"

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'link_whatsapp', 'created_at')
    actions = [exportar_leads_excel]

    # Função para criar o link clicável do WhatsApp
    def link_whatsapp(self, obj):
        # Remove caracteres não numéricos para o link
        clean_phone = "".join(filter(str.isdigit, obj.phone))
        return format_html(
            '<a href="https://wa.me/{}" target="_blank">{}</a>',
            clean_phone,
            obj.phone
        )
    
    link_whatsapp.short_description = 'Whatsapp'

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'description')

@admin.register(Sales_Dashboard)
class SalesDashboardAdmin(admin.ModelAdmin):
    list_display = ('lead', 'user', 'service_interested', 'budget', 'status', 'created_at')
    list_filter = ('status', 'service_interested', 'user')
    search_fields = ('lead__name', 'user__username')