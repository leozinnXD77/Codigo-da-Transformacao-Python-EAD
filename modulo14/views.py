from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from modulo14.models import Produto
from modulo14.forms import ProdutoForm

def produto_list(request):
    query = request.GET.get('q', '')
    if query:
        produtos_list = Produto.objects.filter(nome__icontains=query)
    else:
        produtos_list = Produto.objects.all().order_by('id')

    paginator = Paginator(produtos_list, 5) 
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    return render(request, 'produtos/produto_list.html', {'produtos': produtos, 'query': query})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/produto_form.html', {'form': form})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/produto_form.html', {'form': form})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})