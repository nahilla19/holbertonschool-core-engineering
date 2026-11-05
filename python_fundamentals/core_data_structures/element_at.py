#!/usr/bin/env python3


def element_at(my_list, idx):
    """Return an element, or none for an invalid index."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
