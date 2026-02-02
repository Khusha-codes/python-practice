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
Returns a dictionary containing month-wise, tag-wise counts.

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

The function validates the input type and raises a TypeError if the provided input is not a list.
Invalid or malformed entries inside the list are safely ignored and do not affect the final result.
