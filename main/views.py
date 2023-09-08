from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application_name': 'glowventory',
        'name': 'Bella',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)