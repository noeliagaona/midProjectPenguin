from fastapi import APIRouter
from database.conexion_db import db
from bson import json_util
from json import loads

router = APIRouter()
 
@router.get("/specie/all")
def penguin_specie():
    resp = db["pinguinos_size"].distinct("species")
    return resp

@router.get("/island/all")
def penguin_specie():
    resp = db["pinguinos_size"].distinct("island")
    return resp

@router.get("/specie/{specie}")
def penguin_specie(specie:str):
    filter = {"species":specie.capitalize()}
    project = {"_id":0}
    resp = db["pinguinos_size"].find(filter, project)
    return loads(json_util.dumps(resp))

@router.get("/island/{island}")
def penguin_island(island:str):
    filter = {"island":island.capitalize()}
    project = {"_id":0, "island":1, "species":1}
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

