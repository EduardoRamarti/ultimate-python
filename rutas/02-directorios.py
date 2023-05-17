from pathlib import Path

# path = Path("directorio")
path = Path("rutas")


# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-felix")


# El método iterdir() devuelve un iterador que enumera todos los elementos (archivos y directorios) dentro del directorio path
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

# El método glob(pattern) se utiliza para buscar archivos que coincidan con el patrón especificado. En este caso, el patrón "*.py" busca todos los archivos con extensión ".py" en el directorio.
archivos = [p for p in path.glob("*.py")]
print(archivos)

# El patrón "**/*.py" utilizado con el método glob() busca recursivamente en todos los subdirectorios del directorio path
archivos = [p for p in path.glob("**/*.py")]
print(archivos)

# El método rglob(pattern) es similar a glob(), pero realiza una búsqueda recursiva en todos los subdirectorios sin necesidad de especificar "**/" en el patrón.
archivos = [p for p in path.rglob("*.py")]
print(archivos)
