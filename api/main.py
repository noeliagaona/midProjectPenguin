from fastapi import FastAPI
from routers import penguins_info


app = FastAPI()
app.include_router(penguins_info.router)

@app.get("/")
def root():
    return {"mensaje":"Mi primera API"}
#aa



