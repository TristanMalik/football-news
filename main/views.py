from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406409196',
        'name': 'Muhammad Tristan Malik Anbiya',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
