from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque', 'ativo', 'data_cadastro')
    list_filter = ('ativo', 'data_cadastro')
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'ativo', 'quantidade_estoque')
    readonly_fields = ('data_cadastro',)
    actions = ['ativar_produtos', 'desativar_produtos']

    # Para exibir a imagem no admin
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'preco', 'quantidade_estoque', 'ativo')
        }),
        ('Imagem', {
            'fields': ('imagem',)
        }),
        ('Informações Adicionais', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',)
        }),
    )

    def ativar_produtos(self, request, queryset):
        queryset.update(ativo=True)
    ativar_produtos.short_description = "Ativar produtos selecionados"
    
    def desativar_produtos(self, request, queryset):
        queryset.update(ativo=False)
    desativar_produtos.short_description = "Desativar produtos selecionados"