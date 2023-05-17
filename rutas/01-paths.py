from pathlib import Path  # importa la clase Path de la biblioteca pathlib

# Path(r"C:\Archivos de programa\Minecraft")  # raw string
# Path("/usr/bin") -> este y el de arriba son rutas absolutas
# Path("")
# Path.home() me muestra el directorio home
# Path("one/__init__.py") muestra la ruta relativa del archivo __init__.py


# instancia de  Path, representa la ruta relativa de "hola-mundo/mi_archivo.py"
path = Path("hola-mundo/mi_archivo.py")
path.is_file()  # devuelve True si es un archivo, False de lo contrario
path.is_dir()  # devuelve True si es un directorio, False de lo contrario
path.exists()  # devuelve True si existe la ruta, False de lo contrario

print(
    path.name,  # nombre del archivo
    path.stem,  # nombre del archivo sin extencion
    path.suffix,  # devuelve la extencion del archivo
    path.parent,  # devuelve la ruta padre, 'hola-mundo'
    path.absolute()  # devuelve la ruta absoluta completa
)


# En esta línea, se crea una nueva instancia de Path llamada p que tiene el mismo directorio y extensión que path, pero con un nombre de archivo diferente
# se reemplaza el nombre de archivo de path por "chanchito.py".
p = path.with_name("chanchito.py")
print(p)

# El método with_suffix() permite cambiar la extensión del archivo.
p = path.with_suffix(".bat")
print(p)

# El método with_stem() permite cambiar el nombre del archivo sin modificar la extensión.
p = path.with_stem("feliz")
print(p)
