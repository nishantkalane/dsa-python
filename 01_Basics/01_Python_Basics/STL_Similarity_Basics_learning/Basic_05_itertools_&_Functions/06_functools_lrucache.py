#"If you've already calculated this input, remember the answer and reuse it."
from functools import lru_cache

@lru_cache(maxsize=None)
def feb(n):
    if n<2:
        return n
    return feb(n-1) + feb(n-2)

print(feb(6))