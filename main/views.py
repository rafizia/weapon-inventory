from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Weapentory',
        'name': 'Muhammad Rafi Zia Ulhaq',
        'class': 'PBP B',
    }

    return render(request, "main.html", context)
