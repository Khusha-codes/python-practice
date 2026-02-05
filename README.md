# Python-Practice
My Python learning repository for GSoC preparation.


## FizzBuzz Program

A simple Python program that prints Fizz, Buzz, and FizzBuzz based on
divisibility rules and also counts their occurrences.

## Monthly Issue Counter

This module provides a reusable function to count issues grouped by
month and tag from event logs.

### Function
`monthly_issue(events)`

### Input Format 
Each event must follow this format:

[TAG] YYYY-MM-DD description

Invalid or malformed entries are ignored.

### Output
The function guarantees stable output:
- Months are sorted chronologically
- Tags are sorted alphabetically

This ensures predictable results for testing and reuse.
#### Example

```python
from monthly_issue_counter import monthly_issue

events = [
    "[BUG] 2024-01-10 Login crash",
    "[FEATURE] 2024-01-12 Dark mode"
]

result = monthly_issue(events)
print(result)
```

### Reusability 

The same function can be reused for other domains such as sales or
category-based data, as long as the input follows:

[CATEGORY] YYYY-MM-DD description

### Error Handling

- Raises `TypeError` if input is not a list
- Safely ignores:
  - Non-string entries
  - Malformed event strings
  - Incorrect date formats
