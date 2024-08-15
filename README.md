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

