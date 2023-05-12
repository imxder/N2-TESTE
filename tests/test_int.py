import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.task import Task
from src.task_manager import TaskManager

def test_task_manager_integration():
    
    task_manager = TaskManager()

    task_manager.add_task(Task(1, "Lavar a louça"))
    task_manager.add_task(Task(2, "Passear com o cachorro"))
    task_manager.add_task(Task(3, "Fazer compras no mercado"))

    tasks = task_manager.list_tasks()
    assert len(tasks) == 3
    assert tasks[0].task_id == 1
    assert tasks[0].description == "Lavar a louça"
    assert not tasks[0].done
    assert tasks[1].task_id == 2
    assert tasks[1].description == "Passear com o cachorro"
    assert not tasks[1].done
    assert tasks[2].task_id == 3
    assert tasks[2].description == "Fazer compras no mercado"
    assert not tasks[2].done

    task_manager.mark_task_done(2)

    tasks = task_manager.list_tasks()
    assert len(tasks) == 3
    assert tasks[0].task_id == 1
    assert tasks[0].description == "Lavar a louça"
    assert not tasks[0].done
    assert tasks[1].task_id == 2
    assert tasks[1].description == "Passear com o cachorro"
    assert tasks[1].done
    assert tasks[2].task_id == 3
    assert tasks[2].description == "Fazer compras no mercado"
    assert not tasks[2].done

    task_manager.remove_task(1)

    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].task_id == 2
    assert tasks[0].description == "Passear com o cachorro"
    assert tasks[0].done
    assert tasks[1].task_id == 3
    assert tasks[1].description == "Fazer compras no mercado"
    assert not tasks[1].done