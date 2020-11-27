from django.shortcuts import render
from . import form
from . models import personas, productos
from django.http import Http404

# Create your views here.

def facturalia(request):
    return render(request,'facturacion/facturalia.html',{})

def consulta_contacto(request):
    
    if request.method == 'POST':
        fc = form.consulta_contacto_frm(request.POST)
        if fc.is_valid():
            r = fc.cleaned_data['apellido_contacto']
            listado = personas.objects.filter(apellido = r)
    else:
            listado=personas.objects.all()
            fc=form.consulta_contacto_frm
    
    try:
        return render(request,'facturacion/facturalia_contacto.html',{'formulario':fc,'lista':listado})
    except UnboundLocalError:
        return render(request,'facturacion/facturalia_contacto.html',{'formulario':fc,'lista':['',]})

def consulta_producto(request):
    
    if request.method == 'POST':
        fc = form.consulta_producto_frm(request.POST)
        if fc.is_valid():
            r = fc.cleaned_data['nombre_producto']
            listado = productos.objects.filter(nombre__contains = r)
    else:
            listado=productos.objects.all()
            fc=form.consulta_producto_frm
    
    try:
        return render(request,'facturacion/facturalia_producto.html',{'formulario':fc,'lista':listado})
    except UnboundLocalError:
        return render(request,'facturacion/facturalia_producto.html',{'formulario':fc,'lista':['',]})
