from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name' : 'Weapentory',
        'name': request.user.username,
        'class': 'PBP B',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        messages.success(request, 'Berhasil menambahkan ' + request.POST.get('amount') + ' item ke inventory')
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'message': 'Item berhasil dihapus'})
    except Item.DoesNotExist:
        return JsonResponse({'message': 'Item tidak ditemukan'}, status=404)

def increment_amount(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

def decrement_amount(request, item_id):
    item = Item.objects.get(pk=item_id)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        delete_item(request, item_id)
    return redirect('main:show_main')

def edit_product(request, id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_item_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        type = request.POST.get("type")
        atk = request.POST.get("atk")
        rarity = request.POST.get("rarity")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Item(name=name, type=type, atk=atk, rarity=rarity, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


    