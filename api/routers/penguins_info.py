from fastapi import APIRouter
from database.conexion_db import db
from bson import json_util
from json import loads

router = APIRouter()
 
# lista de especies 
@router.get("/specie/all")
def penguin_specie():
    resp = db["pinguinos_size"].distinct("species")
    return resp

# lista de islas
@router.get("/island/all")
def penguin_specie():
    resp = db["pinguinos_size"].distinct("island")
    return resp

# información por especie
@router.get("/specie/{specie}")
def penguin_specie(specie:str):
    filter = {"species":specie.capitalize()}
    project = {"_id":0}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get("/pinguinos/{specie}/{island}")
def penguin_island(specie:str, island:str):
    filter = {"species":specie.capitalize(),"island":island.capitalize()}
    project = {"_id":0, "island":1, "species":1}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get("/island/{island}/{sex}")
def penguin_island(island:str, sex:str):
    filter = {"island":island.capitalize(), "sex": sex.upper()}
    project = {"_id":0, "species":1, "island":1, "sex":1}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get("/sex/{sex}")
def penguin_island(sex:str):
    filter = {"sex":sex.upper()}
    project = {"_id":0, "island":1, "species":1, "sex":1}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get("/culmen")
def penguin_culmen():
    filter = {}
    project = {"_id":0, "species":1, "culmen_length_mm":1, "culmen_depth_mm":1}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get('/poblacion/islas')
def poblacion_islas():
    filter={}
    project={'island':1,'_id':0}
    data_pinguinos = db["pinguinos_size"].find(filter, project)
    pob_islas={}  
    for pinguino in data_pinguinos:
        if pinguino['island'] in list(pob_islas.keys()):
            pob_islas[pinguino['island']] += 1
        else:
            pob_islas[pinguino['island']]=1
    return pob_islas

@router.get("/media/peso/especies")
def media_peso_especies():
    
    filter={}
    project={'species':1, '_id':0,'body_mass_g':1}
    data_pinguinos=db["pinguinos_size"].find(filter, project)
    media_peso_pinguino={} 
    num_especies={}
    for pinguino in data_pinguinos:
        
        if pinguino['species'] in list(media_peso_pinguino.keys()):
            media_peso_pinguino[pinguino['species']] +=pinguino['body_mass_g']
            num_especies[pinguino['species']]+=1 
        else:
            media_peso_pinguino[pinguino['species']]=pinguino['body_mass_g'] 
            num_especies[pinguino['species']]=1 
    for especies, peso, in media_peso_pinguino.items():
        media_peso_pinguino[especies]= round(peso/num_especies[especies], 2)
    return media_peso_pinguino