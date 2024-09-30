import shutil
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

# Inicializa la consola
console = Console()

def replicate_file(file_path, destination_path, count):
    nombre_archivo = os.path.basename(file_path)
    nombre_base, extension = os.path.splitext(nombre_archivo)

    for i in range(count):
        replicated_file_path = os.path.join(destination_path, f'{nombre_base}copia{i}{extension}')
        shutil.copyfile(file_path, replicated_file_path)

def replicate_directory(source_dir, destination_dir, counts):
    for root, dirs, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        destination_subdir = os.path.join(destination_dir, relative_path)
        os.makedirs(destination_subdir, exist_ok=True)

        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()

            if file_extension in counts:
                replicate_file(file_path, destination_subdir, counts[file_extension])
            else:
                console.print(f"[red][!][/red] Tipo de archivo no reconocido: [yellow]{file_path}[/yellow]. No se replicará.")

# Presentación de Redes Sociales y Creador
def show_info():
    panel = Panel(
        "[bold cyan] Black Hat- GOD[/bold cyan]",
        title="[bold magenta]Información del Creador[/bold magenta]",
        subtitle="Redes Sociales",
        border_style="magenta"
    )
    console.print(panel)

    console.print("[bold green]@SupremoN9[/bold green]")
    console.print("[bold green]@SupremoN9[/bold green]")
    console.print("[bold yellow]Created by :SupremoN9[/bold yellow]")
    console.print("\n")

show_info()

# Menú de opciones para el usuario
table = Table(title="[bold cyan]Selecciona una opción:[/bold cyan]")
table.add_column("Opción", justify="center", style="cyan", no_wrap=True)
table.add_column("Descripción", justify="center", style="white")

table.add_row("1", "base de datos")
table.add_row("2", "gen money")

console.print(table)

opcion = int(console.input("[bold cyan]fuck (1 o 2): ")[0])

# Opción 1: Replicar un archivo
if opcion == 1:
    num_replicas = int(console.input("[bold cyan]¿masivo?: ")[0])
    archivo_ruta = console.input("[bold cyan]ruta: ")
    destino_ruta = console.input("[bold cyan]Introduce la ruta completa del directorio donde se guardarán las réplicas: ")

    if not os.path.exists(destino_ruta):
        console.print(f"[red][!][/red] El directorio [yellow]{destino_ruta}[/yellow] no existe. Por favor, introduce una ruta válida.")
        exit()

    for i in range(num_replicas):
        ruta_destino = os.path.join(destino_ruta, f'{os.path.basename(archivo_ruta)}_copia{i}')
        shutil.copyfile(archivo_ruta, ruta_destino)

    console.print(f"[green][✓][/green] pitudo N9. GOD [yellow]{num_replicas}[/yellow] veces en [yellow]{destino_ruta}[/yellow].")

# Opción 2: Replicar una carpeta completa
elif opcion == 2:
    carpeta_ruta = console.input("[bold cyan]Introduce la ruta completa de la carpeta a replicar: ")
    destino_ruta = console.input("[bold cyan]Introduce la ruta completa del directorio donde se guardarán las réplicas: ")

    if not os.path.exists(carpeta_ruta):
        console.print(f"[red][!][/red] La carpeta [yellow]{carpeta_ruta}[/yellow] no existe. Por favor, introduce una ruta válida.")
        exit()

    if not os.path.exists(destino_ruta):
        console.print(f"[red][!][/red] El directorio [yellow]{destino_ruta}[/yellow] no existe. Por favor, introduce una ruta válida.")
        exit()

    num_imagenes = int(console.input("[bold cyan]¿Cuántas réplicas deseas crear de imágenes?: "))
    num_videos = int(console.input("[bold cyan]¿Cuántas réplicas deseas crear de videos?: "))
    num_archivos = int(console.input("[bold cyan]¿Cuántas réplicas deseas crear de documentos/archivos?: "))

    counts = {
        '.jpg': num_imagenes,
        '.jpeg': num_imagenes,
        '.png': num_imagenes,
        '.gif': num_imagenes,
        '.mp4': num_videos,
        '.avi': num_videos,
        '.mkv': num_videos,
        '.doc': num_archivos,
        '.docx': num_archivos,
        '.pdf': num_archivos,
        '.txt': num_archivos,
        '.apk': num_archivos,
    }

    replicate_directory(carpeta_ruta, destino_ruta, counts)

    console.print(f"[green][✓][/green] Replicación de la carpeta completada en [yellow]{destino_ruta}[/yellow].")
else:
    console.print("[red][!][/red] Opción no válida. Elige 1 o 2.")
