# Python refresher

## Sources

- https://www.youtube.com/watch?v=t8pPdKYpowI

## Notes

### Accepting user input

```bash
name = input("Please enter your age: ")
```

### Error handling with `try/except`

```bash
def validate_and_execute(days):
    try:
        user_input = int(days)
        if user_input > 0:
            print("You entered a valid number")
        elif user_input == 0:
            print("Please enter a valid positive number")
    except ValueError:
        print("Your input ins not a valid number.")
```

### Conversions

```python
# Comma-separated values in a string to a list
input_string = "10, 15, 25, 8"
output_list = input_string.split(", ")

# List to a delimieter-separated string
input_list = ["John", "Jane", "Mark"]
output_string = ", ".join(input_list) # you specify the delimeter first and call the `join` function on it

```
