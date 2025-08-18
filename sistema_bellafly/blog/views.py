from django.shortcuts import render
from products.models import Produto, Roupa, ConjuntoRoupa, KitBeleza, Perfumaria

def index(request):
    categoria = request.GET.get('categoria', 'perfumaria')
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
    context = {'produtos': produtos, 'categoria': categoria}
    return render(request, template_name='index.html', context=context)