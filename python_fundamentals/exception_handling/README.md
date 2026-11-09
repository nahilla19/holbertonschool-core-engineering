# Exception Handling

This directory contains exercises on handling exceptions in Python. Task 0,
**Safe list printing**, is implemented in `safe_print_list.py`.

`safe_print_list(my_list=[], x=0)` prints up to `x` list elements consecutively
on one line, then prints a newline. If `x` is larger than the list, it stops
when the next index raises `IndexError`; the function returns the number of
elements it actually printed. The exercise implementation uses `try`/`except`
and does not import modules or call `len()`.

Run the style and syntax checks from this directory with:

```sh
python3 -m pycodestyle safe_print_list.py
python3 -m py_compile safe_print_list.py
```
