from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Inicio():
    return {"mensaje": "Hola aprendices 3407180"}

@app.get("/saludar")
def Saludar():
    return {"mensaje": "¡Hola, bienvenido a FastAPI!"}

@app.get("/hora")
def hora_actual():
    from datetime import datetime
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"hora_actual": hora}

@app.get("/saludar/{nombre}/{apellido}/{edad}")
def Saludar_completo(nombre: str, apellido: str, edad: int):
    return {"mensaje": f"¡Hola soy {nombre} {apellido} y tengo {edad} años!"}

@app.get("/amigos")
def lista_amigos():
    amigos = [
        {"id": 1, "nombre": "juan",   "edad": 25},
        {"id": 2, "nombre": "maria",  "edad": 30},
        {"id": 3, "nombre": "pedro",  "edad": 28},
        {"id": 4, "nombre": "luis",   "edad": 22},
        {"id": 5, "nombre": "carlos", "edad": 27}
    ]
    return {"amigos": amigos}

@app.get("/amigos/{amigos_id}")
def un_amigo(amigos_id: int):
    amigos = [
        {"id": 1, "nombre": "juan",   "edad": 25},
        {"id": 2, "nombre": "maria",  "edad": 30},
        {"id": 3, "nombre": "pedro",  "edad": 28},
        {"id": 4, "nombre": "luis",   "edad": 22},
        {"id": 5, "nombre": "carlos", "edad": 27}
    ]
    for amigo in amigos:
        if amigo["id"] == amigos_id:
            return {"amigo": amigo}
    return {"mensaje": f"Amigo no encontrado con ID: {amigos_id}"}
