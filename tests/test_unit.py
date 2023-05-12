import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from src.task import Task
from src.task_manager import TaskManager

def test_create_task():
    task = Task(1, "Descrição da tarefa")
    assert task.task_id == 1
    assert task.description == "Descrição da tarefa"
    assert not task.done

def test_task_creation_success():
    task = Task(1, "Descrição da tarefa")
    assert isinstance(task, Task)

def test_add_task():
    task = Task(1, "Descrição da tarefa")
    task_manager = TaskManager()
    task_manager.add_task(task)
    tasks = task_manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0] == task

def test_list_tasks():
    task1 = Task(1, "Tarefa 1")
    task2 = Task(2, "Tarefa 2")
    task_manager = TaskManager()
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    tasks = task_manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0] == task1
    assert tasks[1] == task2

def test_mark_task_done():
    task = Task(1, "Descrição da tarefa")
    task_manager = TaskManager()
    task_manager.add_task(task)
    task_manager.mark_task_done(1)
    assert task.done

def test_remove_task():
    task = Task(1, "Descrição da tarefa")
    task_manager = TaskManager()
    task_manager.add_task(task)
    task_manager.remove_task(1)
    tasks = task_manager.list_tasks()
    assert len(tasks) == 0