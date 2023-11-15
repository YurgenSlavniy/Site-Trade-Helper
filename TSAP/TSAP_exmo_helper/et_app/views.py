from django.shortcuts import render
from django.http import HttpResponse
import requests
import random

def index(request):
    return render(request, "index.html")

def about(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    currents = []
    for el in currency_pairs:
        pair = el.split(sep='_')
        currents.append(pair[0])
        currents.append(pair[1])
    curs = set(currents)
    
    return render(request, "about.html", context={"currents":len(curs), "curent_pairs": len(currency_pairs)})

def currents(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    currents = []
    for el in currency_pairs:
        pair = el.split(sep='_')
        currents.append(pair[0])
        currents.append(pair[1])
    curs = set(currents)
    return render(request, "currents.html", context={"currents":curs}) 

def current_pairs(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    return render(request, "currents.html", context={"currents":currency_pairs}) 

def current_prices(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    pair_info = {}
    if response.status_code == 200:
        currency_pairs = response.json().keys()
        currency_pairs_val = response.json().values()
    valus = []
    for el in currency_pairs_val:
        valus.append(list(el.values())[2])
            
    pair_info = dict(zip(currency_pairs, valus))
    return render(request, "prices_only.html", context={"response":pair_info})


def cur_forms(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    currents = []
    for el in currency_pairs:
        pair = el.split(sep='_')
        currents.append(pair[0])
        currents.append(pair[1])
    curs = set(currents)
    return render(request, "cur_forms.html", context={"currents":curs})
  
    
def cur_forms_answer(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    pair_info = {}
    if response.status_code == 200:
        currency_pairs = response.json().keys()
        currency_pairs_val = response.json().values()
    valus = []
    for el in currency_pairs_val:
        valus.append(list(el.values())[2])
            
    pair_info = dict(zip(currency_pairs, valus))

    current = request.POST["currents"]
    current_pairs = []
    for el in currency_pairs:
        if current in el:
            current_pairs.append(el)
    count_curr_pairs = len(current_pairs)

    current_pairs_prices = []
    for el in current_pairs:
        current_pairs_prices.append(float(pair_info[el]))

    current_pairs_info = dict(zip(current_pairs, current_pairs_prices))
    sorted_values = sorted(current_pairs_info.values())
    sorted_current_pairs_info = {}

    for value in sorted_values:
        for key in current_pairs_info.keys():
            if current_pairs_info[key] == value:
                 sorted_current_pairs_info[key] = current_pairs_info[key]
                 break

    return render(request, "cur_forms_answer.html", 
        context={"curr":current, 
        "currents":current_pairs, 
        "count_cur_pairs":count_curr_pairs,
        "current_pairs_info":current_pairs_info,
        "sorted_current_pairs_info": sorted_current_pairs_info})

def cur_pair_forms_answer(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()

    current_pair = request.POST["current_pairs"]
    values =  response.json()[current_pair]
    
    return render(request, "cur_pair_forms_answer.html", 
        context={"curr":current_pair, "values":values})

def cur_pair_forms(request):
    response = requests.post('https://api.exmo.com/v1.1/ticker')
    if response.status_code == 200:
        currency_pairs = response.json().keys()
    
    return render(request, "cur_pair_forms.html", context={"current_pairs":currency_pairs})


