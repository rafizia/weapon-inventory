from django.shortcuts import render

def show_main(request):
    context = {
        'app-name' : 'Weapentory - Ultimate Weapon Inventory',
        'name': 'Muhammad Rafi Zia Ulhaq',
        'class': 'PBP B',

        'weapon1': 'Sword of Descensions'
    }

    return render(request, "main.html", context)
