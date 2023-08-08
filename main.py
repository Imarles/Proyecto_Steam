from fastapi import FastAPI
from codigo import GPA, JPA, SPPA, EPA, SPA, MPA, Futureprice
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola, Iovan Marles"}


@app.get("/genero/{years}")
def genero(years: str):
    try:
        resault = GPA(years)
        return resault
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/juegos/{years}")
async def juegos(years: str):
    return JPA(years)


@app.get("/specs/{years}")
def specs(years: str):
    try:
        resault = SPPA(years)
        return resault
    except Exception as e:
        return {"error": str(e)}


@app.get("/early_acces/{years}")
def earlyacces(years: str):
    try:
        resault = EPA(years)
        return resault
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/sentiment/{years}")
def sentiment(years: str):
    try:
        resault = SPA(years)
        return resault
    except Exception as e:
        return {"error": str(e)}


@app.get("/metascore/{years}")
def metascore(years: str):
    try:
        resault = MPA(years)
        return resault
    except Exception as e:
        return {"error": str(e)}
    
# ========================================== #
# App de la funcion del modelo de prediccion

@app.get("/Modelo_de_prediccion/{variables}")
def predictor(variables: str):
    try:
        result = Futureprice(variables)
        return result
    except Exception as e:
        return {"error": str(e)}
    