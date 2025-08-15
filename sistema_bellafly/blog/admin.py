# from django.contrib import admin
# from products.models import Produto, Roupa, ConjuntoRoupa, KitBeleza, Perfumaria

# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'preco', 'quantidade_estoque', 'ativo', 'data_cadastro')
#     list_filter = ('ativo', 'data_cadastro')
#     search_fields = ('nome', 'descricao')

# @admin.register(Roupa)
# class RoupaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'tamanho', 'cor', 'preco', 'quantidade_estoque', 'ativo')
#     list_filter = ('tamanho', 'cor', 'ativo')
#     search_fields = ('nome', 'descricao', 'cor')

# @admin.register(ConjuntoRoupa)
# class ConjuntoRoupaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'preco', 'quantidade_estoque', 'ativo')
#     filter_horizontal = ('roupas',)
#     search_fields = ('nome', 'descricao')

# @admin.register(KitBeleza)
# class KitBelezaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'preco', 'quantidade_estoque', 'ativo')
#     filter_horizontal = ('produtos',)
#     search_fields = ('nome', 'descricao')

# @admin.register(Perfumaria)
# class PerfumariaAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'fragrancia', 'volume_ml', 'preco', 'quantidade_estoque', 'ativo')
#     list_filter = ('fragrancia', 'ativo')
#     search_fields = ('nome', 'descricao', 'fragrancia')