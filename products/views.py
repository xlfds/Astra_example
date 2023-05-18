import requests
import io

from zipfile import ZipFile

from django.shortcuts import render

def home(request):
    print ("home is home")
    return render(request, "products/home.html")

def download_export(url="https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"):
    try:
        file = requests.get(url, stream=True)
        zip_file = ZipFile(io.BytesIO(file.content), 'r')
        xml_name = zip_file.namelist()[0]
        raw_xml = zip_file.read(xml_name)
    except IndexError:
        return None

    return raw_xml

def task1(request):
    context = dict()
    context['task'] = "Task3"
    context['total_sum'] = download_export()
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

