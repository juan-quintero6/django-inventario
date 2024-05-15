from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    productos = Producto.objects.all()  # pylint: disable=no-member
    return render(request, 'lista_productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})
