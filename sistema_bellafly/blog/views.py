from django.shortcuts import render
from products.models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, template_name='index.html', context=context)