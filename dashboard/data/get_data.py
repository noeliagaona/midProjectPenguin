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

def get_penguins_by_isla():
    return requests.get(url+"/poblacion/islas").json()   

def get_island_by_penguin(specie, island):
    return requests.get(url+f"/pinguinos/{specie}/{island}").json()   

def get_media_peso():
    return requests.get(url+f"/media/peso/especies").json()
