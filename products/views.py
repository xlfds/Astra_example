import requests
import io
import xmltodict

from zipfile import ZipFile

from django.shortcuts import render


def home(request):
    return render(request, "products/home.html")


def download_export(url="https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"):
    try:
        file = requests.get(url, stream=True)
        zip_file = ZipFile(io.BytesIO(file.content), "r")
        xml_name = zip_file.namelist()[0]
        raw_xml = zip_file.read(xml_name)
        xml_dict = xmltodict.parse(raw_xml)
        xml_dict = xml_dict.get("export_full", None)
    except IndexError:
        return None

    return xml_dict


def get_part_name(part):
    if type(part) == dict:
        name = part.get("@name", None)
        return name if name else None


def get_parts_names(part_item):
    part_names = list()
    if part_item:
        if type(part_item) == list:
            for part in part_item:
                name = get_part_name(part)
                if name:
                    part_names.append(name)
        else:
            name = get_part_name(part_item)
            if name:
                part_names.append(name)
    return part_names


def task1(request):
    context = dict()
    context["task"] = "Task1"

    xml_dict = download_export()
    context["total_sum"] = len(xml_dict["items"]["item"])

    return render(request, "products/home.html", context)


def task2(request):
    context = dict()
    context["task"] = "Task2"

    xml_dict = download_export()
    products = list()
    for item in xml_dict["items"]["item"]:
        name = item.get("@name", None)
        if name:
            products.append({"name": name})

    context["total_sum"] = len(products)
    context["products"] = products
    return render(request, "products/home.html", context)


def task3(request):
    context = dict()
    context["task"] = "Task3"

    xml_dict = download_export()
    products = list()
    for item in xml_dict["items"]["item"]:
        name = item.get("@name", None)
        parts = item.get("parts", None)
        parts_names = list()
        if parts:
            parts = parts.get("part", None)
            if parts:
                if type(parts) == list:
                    for part in parts:
                        part_item = part.get("item", None)
                        parts_names += get_parts_names(part_item)
                else:
                    part_item = parts.get("item", None)
                    parts_names += get_parts_names(part_item)

        if name and parts_names:
            products.append({"name": name, "assembly_parts": parts_names})

    context["total_sum"] = len(products)
    context["products"] = products
    return render(request, "products/home.html", context)
