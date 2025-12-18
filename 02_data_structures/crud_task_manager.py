task = []                               # Inicializa una lista vacía para almacenar las tareas

def add_task():
    new_task = input("Enter new task: ")
    task.append(new_task)               # Agrega la nueva tarea al final de la lista
    print("Task added.")

def view_tasks():
    if not task:                        # Verifica si la lista de tareas está vacía
        print("No tasks available.\n")
    else:
        print("Tasks: ")
        for i, t in enumerate(task, 1): # Enumera las tareas con un índice comenzando en 1
            print(f"{i}. {t}")          # Muestra cada tarea con su número correspondiente

def delete_tasks():
    view_tasks()                        # Muestra las tareas antes de eliminar
    if task:                            # Verifica si hay tareas para eliminar
        try:
            index = int(input("Enter task number to delete: ")) - 1 # Resta 1 para convertir a índice basado en 0
            if 0 <= index < len(task):                              # Verifica si el índice es válido
                removed_task = task.pop(index)                      # Elimina la tarea en el índice especificado
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\t.:Task Manager:.")
    print("1. Add Task / 2. View Tasks / 3. Delete / 4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_tasks()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")