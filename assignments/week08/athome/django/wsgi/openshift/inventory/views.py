from django.shortcuts import render_to_response
from inventory.models import Manufacture, Product

# Display Manufacture and Inventory
def display_manufacture(request, *args, **kwargs):
    return render_to_response('inventory/manu_list.html', {'manufacture': Manufacture.objects.all()})

def display_manu_inventory(request, *args, **kwargs):
    manufacture_name = args[0].upper()
    all_products = Product.objects.all()
    product_dict = {}
    for product in all_products:
        if str(product.product_manufacture).upper() == str(manufacture_name):
            product_dict[product.product_desc] = {'qty': product.product_stock, 'price_euro': product.product_price_euro, 'price_nt': product.product_price_nt}
    return render_to_response('inventory/manu_details.html', {'manufacture': manufacture_name, 'products': product_dict})

# Search for Manufacture
def search_manufacture(request):
    return render_to_response('inventory/search_manufacture.html')

def search(request):
    if 'manufacture' in request.GET and request.GET['manufacture']:
        manufacture = request.GET['manufacture']
        return render_to_response('inventory/search_result.html', {'manufacture': manufacture})
    else:
        return render_to_response('inventory/search_result.html', {'error': True})


