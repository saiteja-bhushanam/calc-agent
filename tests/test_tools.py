import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "agent"))

import tools


def setup_function():
    tools._store.clear()


def test_add():
    assert tools.add(2, 3) == 5


def test_multiply():
    assert tools.multiply(4, 5) == 20


def test_save_list_delete():
    tools.add(1, 1, save_as="x")
    assert tools.list_saved() == {"x": 2}
    assert tools.delete("x") == "Deleted 'x'"
    assert tools.list_saved() == {}


def test_delete_missing():
    assert "not found" in tools.delete("nope")
