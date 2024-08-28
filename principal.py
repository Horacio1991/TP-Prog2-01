import datetime

# Lista donde se van a guardar las tareas
tareas = []

# Validar si la fecha se ingreso en formato dia-mes-año


def validar_fecha(fecha_texto):
    try:
        datetime.datetime.strptime(fecha_texto, '%d-%m-%Y')
        return True
    except ValueError:
        return False

# Cada tarea se agrega como un diccionario, y se guarda en la lista en el archivo .txt


def agregar_tarea(descripcion, fecha):
    if not validar_fecha(fecha):
        print("Fecha no válida. Por favor, use el formato 'DD-MM-YYYY'.")
        return

    tarea = {
        'descripcion': descripcion,
        'fecha': fecha,
        'completada': False
    }
    tareas.append(tarea)
    guardar_tareas('tareas.txt')
    print(f"Tarea agregada: {descripcion}")

# Filtro para traer a la vista las tareas pendientes o completadas


def listar_tareas(filtro=None):
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea['completada'] else "Pendiente"
        if filtro is None or (filtro == 'completadas' and tarea['completada']) or (filtro == 'pendientes' and not tarea['completada']):
            print(f"{i + 1}. {tarea['descripcion']
                              } - {tarea['fecha']} [{estado}]")

# Verifica que el indice este entre 0 y el largo de la lista y cambia el estado de completada a True


def completar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        guardar_tareas('tareas.txt')
        print(f"Tarea completada: {tareas[indice]['descripcion']}")
    else:
        print("Índice de tarea no válido.")

# Verifica que el indice este dentro de los rangos posibles y con el metodo pop elimina la tarea con el indice pasado por parametros


def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas('tareas.txt')
        print(f"Tarea eliminada: {tarea_eliminada['descripcion']}")
    else:
        print("Índice de tarea no válido.")

# Guardar las tareas que estan en la lista en el archivo para la persistencia


def guardar_tareas(archivo):
    with open(archivo, 'w') as file:
        for tarea in tareas:
            completada = '1' if tarea['completada'] else '0'
            linea = f"{tarea['descripcion']},{tarea['fecha']},{completada}\n"
            file.write(linea)

# Cargar las tareas del archivo a la lista


def cargar_tareas(archivo: str) -> None:
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                descripcion, fecha, completada = linea.strip().split(',')
                tarea = {
                    'descripcion': descripcion,
                    'fecha': fecha,
                    'completada': completada == '1'
                }
                tareas.append(tarea)
        print(f"Tareas cargadas desde el archivo '{archivo}'.")
    except FileNotFoundError:
        print(f"El archivo '{
              archivo}' no existe. Comenzando con una lista de tareas vacía.")

# Menu principal


def mostrar_menu() -> None:
    print("\n--- Tareas ---")
    print("1. Agregar Tarea")
    print("2. Completar Tarea")
    print("3. Eliminar Tarea")
    print("4. Listar Tareas Pendientes")
    print("5. Listar Todas las Tareas")
    print("6. Salir")


def main() -> None:
    cargar_tareas('tareas.txt')
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha = input("Ingrese la fecha de la tarea (DD-MM-YYYY): ")
            agregar_tarea(descripcion, fecha)

        elif opcion == '2':
            listar_tareas()
            indice = int(
                input("Ingrese el número de la tarea a completar: ")) - 1
            completar_tarea(indice)

        elif opcion == '3':
            listar_tareas()
            indice = int(
                input("Ingrese el número de la tarea a eliminar: ")) - 1
            eliminar_tarea(indice)

        elif opcion == '4':
            listar_tareas(filtro='pendientes')

        elif opcion == '5':
            listar_tareas()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()
