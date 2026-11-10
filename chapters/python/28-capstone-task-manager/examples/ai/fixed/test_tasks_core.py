# file: examples/ai/fixed/test_tasks_core.py
from pathlib import Path
import pytest
from tasks_core import TaskList, load_tasks, save_tasks


def sample():
    tasks = TaskList()
    tasks.add("Open the cafe", 1)
    tasks.add("Restock milk")
    tasks.add("Call the supplier", 3)
    return tasks


def test_add_keeps_order():
    assert sample().tasks[0].title == "Open the cafe"


def test_add_refuses_empty_title():
    with pytest.raises(ValueError):
        TaskList().add("   ")


def test_add_refuses_bad_priority():
    with pytest.raises(ValueError):
        TaskList().add("Sweep the floor", 5)


def test_complete_counts_from_one():
    tasks = sample()
    tasks.complete(1)
    assert tasks.tasks[0].done and not tasks.tasks[1].done


def test_complete_refuses_missing_number():
    with pytest.raises(ValueError):
        sample().complete(4)


def test_open_tasks():
    tasks = sample()
    tasks.complete(2)
    assert len(tasks.open_tasks()) == 2


def test_save_then_load_gives_same_lines():
    tasks = sample()
    tasks.complete(1)
    save_tasks(Path("saved.json"), tasks)
    loaded = load_tasks(Path("saved.json"))
    assert loaded.lines() == tasks.lines()


def test_missing_file_means_no_tasks():
    assert load_tasks(Path("no_such_file.json")).tasks == []


def test_empty_file_means_no_tasks():
    Path("empty.json").write_text("", encoding="utf-8")
    assert load_tasks(Path("empty.json")).tasks == []


def test_bad_json_gives_clear_message():
    text = '[{"title": "Tea"'
    Path("broken.json").write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        load_tasks(Path("broken.json"))
