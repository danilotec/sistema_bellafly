from django.shortcuts import render
from products.models import Produto, Roupa, ConjuntoRoupa, KitBeleza, Perfumaria
from itertools import chain

def index(request):
    categoria = request.GET.get('categoria', 'perfumaria')
    query = request.GET.get('q', '')  # ← MUDANÇA: valor padrão vazio ao invés de None
    
    if query:  # ← Agora funciona corretamente pois string vazia é falsy
        # Busca em todos os modelos
        roupas = Roupa.objects.filter(ativo=True, nome__icontains=query)
        conjuntos = ConjuntoRoupa.objects.filter(ativo=True, nome__icontains=query)
        kits = KitBeleza.objects.filter(ativo=True, nome__icontains=query)
        perfumaria = Perfumaria.objects.filter(ativo=True, nome__icontains=query)
        diversos = Produto.objects.filter(ativo=True, nome__icontains=query)
        
        # Junta tudo em uma lista
        produtos = list(chain(roupas, conjuntos, kits, perfumaria, diversos))
    else:
        # Comportamento normal por categoria
        if categoria == 'roupas':
            produtos = Roupa.objects.filter(ativo=True)
        elif categoria == 'conjuntos':
            produtos = ConjuntoRoupa.objects.filter(ativo=True)
        elif categoria == 'kits':
            produtos = KitBeleza.objects.filter(ativo=True)
        elif categoria == 'perfumaria':
            produtos = Perfumaria.objects.filter(ativo=True)
        elif categoria == 'diversos':
            produtos = Produto.objects.filter(ativo=True)
        else:
            # Fallback para categoria padrão
            produtos = Perfumaria.objects.filter(ativo=True)
    
    context = {
        'produtos': produtos,
        'categoria': categoria,
        'query': query if query else '',  # ← MUDANÇA: garante que nunca seja None
    }
    return render(request, 'index.html', context)