from django.shortcuts import render, render_to_response
from inventory.models import Manufacture, Product
from orderPipeline.models import sales_person
from django.contrib.auth.decorators import login_required

@login_required
def order1(request, *args, **kwargs):
    manufactures = Manufacture.objects.all()
    request.session.set_test_cookie() #Test Session Cookie
    request.session["fav_color"] = "red" #This is the actual cookie
    return render(request, 'orderPipeline/order1.html', {'manufactures': manufactures})
    
@login_required
def order2(request):
    manu_name = request.POST['manu_name']
    
    if request.session.test_cookie_worked(): # checking test session cookie
        print "The Test Session Cookie Worked"
        print "Now deleting Test Session Cookie"
        request.session.delete_test_cookie()
    if request.session['fav_color']: # checking actual cookie
        print "Your favorite color is: " + request.session['fav_color']
        print "Now deleting fav color cookie"
        del request.session['fav_color']

    # This is ghetto, need to find a better way to query the database
    # tried Product.objects.filter(), Product.objects.get(), etc.
    # https://docs.djangoproject.com/en/1.4/topics/db/queries/
    product_list = []
    for p in Product.objects.all():
        if  str(p.product_manufacture) == manu_name:
            product_list.append(p.product_desc)
    return render(request, 'orderPipeline/order2.html', {'manufacture_name': manu_name, "product_list": product_list})

