"""Plain calculator tools. Kept free of framework imports so they are easy to test."""
from typing import Dict, Optional

_store: Dict[str, float] = {}


def add(a: float, b: float, save_as: Optional[str] = None) -> float:
    """Add two numbers. Optionally save the result under a name."""
    result = a + b
    if save_as:
        _store[save_as] = result
    return result


def multiply(a: float, b: float, save_as: Optional[str] = None) -> float:
    """Multiply two numbers. Optionally save the result under a name."""
    result = a * b
    if save_as:
        _store[save_as] = result
    return result


def delete(name: str) -> str:
    """Delete a previously saved result by name."""
    if name in _store:
        del _store[name]
        return f"Deleted '{name}'"
    return f"'{name}' not found"


def list_saved() -> Dict[str, float]:
    """List all saved results."""
    return dict(_store)
