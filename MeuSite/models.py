from django.db import models
from django.contrib.auth.models import User
class Lead(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Whatsapp")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.name
    
class Sales_Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuário")
    lead = models.ForeignKey(Lead, on_delete=models.PROTECT, verbose_name="Lead")
    service_interested = models.CharField(max_length=100, verbose_name="Serviço de Interesse")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Orçamento")
    status = models.BooleanField(default=False, verbose_name="Fechado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    description = models.TextField(verbose_name="Descrição")


    class Meta:
        verbose_name = "Dashboard de Vendas"
        verbose_name_plural = "Dashboards de Vendas"
