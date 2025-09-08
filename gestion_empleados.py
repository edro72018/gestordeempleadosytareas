#clase empleado y método
class Empleado:
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

    def mostrar_datos_empleado(self):
        return f"Empleado: {self.nombre}, {self.edad} años, puesto: {self.puesto}"

    def solo_nombre_empleado(self):
        return f"{self.nombre}"

class Tarea:
    def __init__(self, titulo, descripcion, empleado_asignado, completado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.empleado_asignado = empleado_asignado
        self.completado = completado

    def mostrar_tarea(self):
        status = "Completado" if self.completado else "Incompleto"
        return f"{self.titulo}\n   Asignado a: {self.empleado_asignado.solo_nombre_empleado()}\n   Status: {status}"

    def solo_nombre_empleado(self):
        return self.nombre

#lista vacia
todos_empleados = []
todas_tareas = []

#datos del empleado
def agregar_empleado():
    nombre_empleado = input("Ingrese el nombre completo del empleado: ")
    while True:
        try:
            edad_empleado = int(input("Ingrese la edad del empleado: "))
            break
        except ValueError:
            print("La edad debe ser un número.")
                
    puesto_empleado = input("Ingrese el puesto del empleado: ")

    nuevo_empleado = Empleado(nombre_empleado, edad_empleado, puesto_empleado)
    todos_empleados.append(nuevo_empleado)
    print("Empleado agregado correctamente.")

#Listado de empleados
def listar_empleados():
    if not todos_empleados:
        print("\n===== Lista de Empleado =====")
        print("- No hay empleados registrados.")
    else:
        print("\n===== Lista de Empleado =====")
        for i, emp in enumerate(todos_empleados, start=1):
            print(f"{i}. {emp.mostrar_datos_empleado()}")
        print("\n\n")

#Eliminar empleados
def eliminar_empleado():
    nombre_empleado = input("Ingrese el nombre del empleado a eliminar: ")
    for i in todos_empleados:
        if i.nombre == nombre_empleado:
            todos_empleados.remove(i)
            print(f"Empleado {nombre_empleado} eliminado correctamente.")
            return
    print(f"No se encontró un empleado con el nombre {nombre_empleado}.")

#Administrador de tareas
def administrador_tareas():
    while True:
        print("\n=== Administrador de tareas ===")
        print("1. Crear tarea.")
        print("2. Mostrar tareas.")
        print("3. Marcar tareas como completadas.")
        print("4. Eliminar tareas.")
        print("0. Atrás")
        try:
            option = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue        
        match option:
            case 0:
                return
            case 1: 
                agregar_tarea()
            case 2:
                mostrar_tarea()
            case 3:
                marcar_completo_tarea()
            case 4:
                eliminar_tarea()
            case _:
                print("Opción inválida\n\n")

def agregar_tarea():
    nombre_tarea = input("Nombre de la tarea: ")
    descripcion_tarea = input("Descripción de la tarea: \n")
    nombre_empleado = input("Nombre del empleado asignado: ")
    status = False

    empleado_asignado = None
    for i in todos_empleados:
        if i.nombre == nombre_empleado:
            empleado_asignado = i
            break

    if empleado_asignado is None:
        print(f"No se encontró el nombre {nombre_empleado}")
        return

    nueva_tarea = Tarea(nombre_tarea, descripcion_tarea, empleado_asignado, status)
    todas_tareas.append(nueva_tarea)
    print("Tarea creada.")

def mostrar_tarea():
    if not todas_tareas:
        print("===== Lista de Tareas =====")
        print("No hay tareas registradas")
    else:
        print("===== Lista de Tareas =====")
        for i, task in enumerate(todas_tareas, start = 1):
            print(f"{i}. {task.mostrar_tarea()}")

def marcar_completo_tarea():
    if not todas_tareas:
        print("===== Lista de Tareas =====")
        print("No hay tareas registradas")
        return

    print("===== Lista de Tareas =====")
    # Mostrar solo las tareas incompletas
    tareas_incompletas = [task for task in todas_tareas if not task.completado]

    if not tareas_incompletas:
        print("Todas las tareas ya están completas 🎉")
        return

    for i, task in enumerate(tareas_incompletas, start=1):
        print(f"{i}. {task.mostrar_tarea()}")

    while True:
        try:
            idx = int(input("Ingresa el índice de la tarea que quieres marcar como completa: "))
            if 1 <= i <= len(tareas_incompletas):
                tarea = tareas_incompletas[i - 1]
                tarea.completado = True
                print(f"✅ La tarea '{tarea.titulo}' fue marcada como completada.")
                break
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def eliminar_tarea():
    if not todas_tareas:
        print("===== Lista de Tareas =====")
        print("No hay tareas registradas")
        return
    else:
        print("===== Lista de Tareas =====")
        for i, task in enumerate(todas_tareas, start = 1):
            print(f"{i}. {task.mostrar_tarea()}")
    while True:
        try:
            tarea_eliminar = int(input("¿Qué tarea deseas eliminar? (índice): "))

            if 1 <= tarea_eliminar <= len(todas_tareas):  # Validar índice
                tarea = todas_tareas.pop(tarea_eliminar - 1)  # quitar de la lista
                print(f"Tarea '{tarea.titulo}' eliminada")
                break
            else:
                print("Índice fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Dato inválido. Ingresa un número.")



#Menú principal
def menu():
    while True:
        print("\n======= Menú de Gestión de Empleados =======")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado")
        print("4. Tareas")
        print("0. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '0':
            print("Ok, baiii!")
            break
        elif opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            listar_empleados()
        elif opcion == '3':
            eliminar_empleado()
        elif opcion == '4':
            administrador_tareas()
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n\n")

if __name__ == "__main__":
    menu()