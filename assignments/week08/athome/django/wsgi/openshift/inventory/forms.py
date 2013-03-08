from django.shortcuts import render, render_to_response
from inventory.models import Manufacture, Product
from django.forms import ModelForm

# Add Manufacture - User

class ManufactureForm(ModelForm):
    class Meta:
        model = Manufacture

# Below are view functions, keeping them in one file during learning

def add_manufacture(request):
    form = ManufactureForm()
    return render(request, 'inventory/add_manufacture.html', {'form': form})

def add_manufacture_submit(request):
    new_name = request.POST['manufacture_name']
    new_manufacture = Manufacture(manufacture_name=new_name)
    new_manufacture.save()
    return render_to_response('inventory/add_manufacture_submit.html', {'new_manufacture': new_name})

