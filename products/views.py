from django.shortcuts import render

def home(request):
    print ("home is home")
    return render(request, "products/home.html")

def task1(request):
    context = dict()
    context['task'] = "Task3"
    context['total_sum'] = 20
    return render(request, "products/home.html", context)

def task2(request):
    context = dict()
    context['task'] = "Task3"
    context['products'] = [{"name": "ggg"}, {"name": "ttt"}]
    return render(request, "products/home.html", context)

def task3(request):
    context = dict()
    context['task'] = "Task3"
    context['products'] = [{"name": "ggg", "assembly_parts": ["fff", "hhh"]}]
    return render(request, "products/home.html", context)

