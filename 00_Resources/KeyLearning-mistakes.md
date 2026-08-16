##  Common Mistakes to Watch For - Patterns
- Wrong `range()` boundary — off by one
- Hardcoded value instead of using a variable
- Variable initialized in the wrong scope (inside vs outside outer loop, inside if you want to have it new everytime and outside if you want to keep it once)
- Increment `p += 1` placed in the wrong loop (per element vs per row)
- Forgetting to reset a variable that should restart each row
- Accidentally continuing a variable that should reset
- Duplicate middle row when combining two patterns
- Inconsistent space width in centered patterns breaking alignment
- Calling `print()` before the full row is complete
- Function name and function call not matching
- Writing `=` instead of `==` in if __name__ == "__main()__"
- Flipping a variable between 0 and 1 can be done by changing the variable using math shortcut of k= 1-k
- Incrementing can be done properly if we want the mirror pattern and for the second time -by subtracting beforehand of printing the second time(i.e the mirror side)
- ascii A= 65  , a = 97, 0 =48
- use chr(ascii) function to print the letter at particular ascii index

Last Updated: 16-Aug-2026