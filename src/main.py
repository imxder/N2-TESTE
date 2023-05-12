from task import Task
from task_manager import TaskManager


def main():
    
    task_manager = TaskManager()
    
    task_manager.add_task(Task(1, "Lavar a louça"))
    task_manager.add_task(Task(2, "Passear com o cachorro"))
    task_manager.add_task(Task(3, "Fazer compras no mercado"))
    
    print("Tarefas existentes:")
    for task in task_manager.list_tasks():
        print(f"  [{task.id}] {task.description} - {'Concluída' if task.done else 'Pendente'}")
    
    task_manager.mark_task_done(2)
 
    task_manager.remove_task(1)
    
    print("Tarefas existentes:")
    for task in task_manager.list_tasks():
        print(f"  [{task.id}] {task.description} - {'Concluída' if task.done else 'Pendente'}")
    
if __name__ == "__main__":
    main()