"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
from collections import Counter

def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str

    Output:
    str
    """
    # Your code here
    counted_s = Counter(s)
    sorted_letters = sorted(counted_s.items(), key=lambda kv: -kv[1])
    print(sorted_letters)
    string = ""
    for letter, value in sorted_letters:
        letters = letter * value
        string += letters
    return string 

print(frequency_sort('freefreee free'))