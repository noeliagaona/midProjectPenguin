import requests

url = "http://127.0.0.1:8000"

def get_species_all():
    return requests.get(url+"/specie/all").json()

def get_island_all():
    return requests.get(url+"/island/all").json()

def get_species(specie):
    return requests.get(url+f"/specie/{specie}").json()

def get_island(island):
    return requests.get(url+f"/island/{island}").json()

def get_sex(sex):
    return requests.get(url+f"/sex/{sex}").json()

def get_culmen():
    return requests.get(url+"/culame").json()
