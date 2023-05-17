from pathlib import Path
import db
import graphql
import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphlql": "esto es graphql"
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcionamiento")


list(map(load, paths))
