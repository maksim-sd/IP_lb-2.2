from django.shortcuts import render
from django.http import HttpResponseNotFound
import json, os
from datetime import datetime


def advanteges_load():
    if os.path.exists("./data/advanteges.json"):
        with open("./data/advanteges.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def tariffs_load():
    if os.path.exists("./data/tariffs.json"):
        with open("./data/tariffs.json", "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def add_bid(bid):
    with open("./data/bid.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        data.append({f"bid-{datetime.now().strftime("%d/%m%/Y-%H:%M:%S")}": bid})

    with open("./data/bid.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def index(request):
    return render(request, "index.html")

def advanteges(request):
    data = {"advanteges": advanteges_load()}
    return render(request, "advanteges.html", context=data)

def tariffs(request):
    data = {"tariffs": tariffs_load()}
    return render(request, "tariffs.html", context=data)

def contacts(request):
    return render(request, "contacts.html")

def send_bid(request):
    name = request.POST.get("name", "Undefied")
    phone = request.POST.get("phone", 0)
    bid_dict = {
        "name": name,
        "phone": phone
    }

    add_bid(bid_dict)
    return render(request, "contacts.html")