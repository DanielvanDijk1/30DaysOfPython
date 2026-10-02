# Day 2 Notes

# Functions
| Function | What it does |
|---|---|
| `abs()` | Returns absolute value. |
| `all()` | Returns `True` if every item is truthy. |
| `any()` | Returns `True` if at least one item is truthy. |
| `ascii()` | Converts an object to escaped ASCII text. |
| `bin()` | Converts an integer to binary text. |
| `bool()` | Converts a value to `True` or `False`. |
| `breakpoint()` | Pauses execution for debugging. |
| `bytearray()` | Creates a mutable sequence of bytes. |
| `bytes()` | Creates an immutable byte sequence. |
| `callable()` | Checks whether an object can be called like a function. |
| `chr()` | Converts a Unicode number to a character. |
| `classmethod()` | Defines a method that receives the class. |
| `compile()` | Compiles text into executable code. |
| `complex()` | Creates a complex number. |
| `delattr()` | Deletes an object attribute. |
| `dict()` | Creates a dictionary. |
| `dir()` | Lists available names or attributes. |
| `divmod()` | Returns the quotient and remainder together. |
| `enumerate()` | Adds index numbers while looping. |
| `eval()` | Evaluates a string as an expression. |
| `exec()` | Executes a string as Python code. |
| `filter()` | Keeps items satisfying a condition. |
| `float()` | Converts a value to a decimal number. |
| `format()` | Formats a value as text. |
| `frozenset()` | Creates an immutable set. |
| `getattr()` | Gets an attribute by name. |
| `globals()` | Returns the global namespace dictionary. |
| `hasattr()` | Checks whether an object has an attribute. |
| `hash()` | Returns an object’s hash value. |
| `help()` | Shows Python documentation. |
| `hex()` | Converts an integer to hexadecimal text. |
| `id()` | Returns an object’s identity number. |
| `input()` | Reads text entered by the user. |
| `int()` | Converts a value to an integer. |
| `isinstance()` | Checks whether a value has a specified type. |
| `issubclass()` | Checks whether a class inherits from another class. |
| `iter()` | Creates an iterator from an iterable. |
| `len()` | Returns the number of items. |
| `list()` | Creates a list. |
| `locals()` | Returns the current local namespace. |
| `map()` | Applies a function to every item. |
| `max()` | Returns the largest item. |
| `memoryview()` | Views byte data without copying it. |
| `min()` | Returns the smallest item. |
| `next()` | Gets the next item from an iterator. |
| `object()` | Creates a basic Python object. |
| `oct()` | Converts an integer to octal text. |
| `open()` | Opens a file. |
| `ord()` | Converts a character to its Unicode number. |
| `pow()` | Raises a number to a power. |
| `print()` | Displays output. |
| `property()` | Creates managed object attributes. |
| `range()` | Generates a sequence of numbers. |
| `repr()` | Returns an unambiguous representation as text. |
| `reversed()` | Iterates over items backwards. |
| `round()` | Rounds a number. |
| `set()` | Creates a mutable set of unique items. |
| `setattr()` | Sets an object attribute by name. |
| `slice()` | Creates a slicing specification. |
| `sorted()` | Returns items in sorted order. |
| `staticmethod()` | Defines a method without automatic `self` or `cls`. |
| `str()` | Converts a value to text. |
| `sum()` | Adds numeric items. |
| `super()` | Accesses methods from a parent class. |
| `tuple()` | Creates a tuple. |
| `type()` | Returns an object’s type. |
| `vars()` | Returns an object’s attribute dictionary. |
| `zip()` | Combines items from multiple iterables. |
| `__import__()` | Imports a module internally. |

# Key words

## Constants and logical operators

| Keyword | Category | What it does |
|---|---|---|
| `True` | Constant | Represents a true Boolean value. |
| `False` | Constant | Represents a false Boolean value. |
| `None` | Constant | Represents no value or the absence of a value. |
| `and` | Logical operator | True when both conditions are true. |
| `or` | Logical operator | True when at least one condition is true. |
| `not` | Logical operator | Reverses a Boolean value. |
| `is` | Identity operator | Checks whether two names refer to the same object. |
| `in` | Membership operator | Checks whether a value exists inside a collection. |

## Conditional logic

| Keyword | Category | What it does |
|---|---|---|
| `if` | Conditional | Runs code when a condition is true. |
| `elif` | Conditional | Tests another condition if earlier conditions were false. |
| `else` | Conditional | Runs code when all preceding conditions are false. |
| `match` | Pattern matching | Compares a value against defined patterns. |
| `case` | Pattern matching | Defines a pattern inside a `match` statement. |

## Loops and loop control

| Keyword | Category | What it does |
|---|---|---|
| `for` | Loop | Iterates over items in a collection. |
| `while` | Loop | Repeats code while a condition is true. |
| `break` | Loop control | Exits a loop immediately. |
| `continue` | Loop control | Skips to the next loop iteration. |
| `pass` | Placeholder | Does nothing; used where code is required syntactically. |

## Functions and generators

| Keyword | Category | What it does |
|---|---|---|
| `def` | Function | Defines a reusable function. |
| `return` | Function control | Sends a result back from a function. |
| `lambda` | Function | Creates a small anonymous function. |
| `yield` | Generator | Produces a value while pausing the function. |

## Classes and object-oriented programming

| Keyword | Category | What it does |
|---|---|---|
| `class` | Class | Defines a class or object blueprint. |
| `super` | Inheritance | Accesses methods from a parent class. |
| `self` | Convention | Refers to the current object; technically not a keyword. |

## Imports and namespaces

| Keyword | Category | What it does |
|---|---|---|
| `import` | Import | Loads a module. |
| `from` | Import | Imports a specific item from a module. |
| `as` | Alias | Gives an imported item another name. |
| `global` | Scope | Refers to a variable in the global scope. |
| `nonlocal` | Scope | Refers to a variable in an enclosing function scope. |

## Error handling

| Keyword | Category | What it does |
|---|---|---|
| `try` | Error handling | Starts code that might cause an error. |
| `except` | Error handling | Handles a specific error. |
| `else` | Error handling | Runs if the `try` block succeeds. |
| `finally` | Error handling | Runs whether an error occurs or not. |
| `raise` | Error handling | Manually triggers an exception. |
| `assert` | Debugging | Checks a condition and raises an error if false. |

## Asynchronous programming

| Keyword | Category | What it does |
|---|---|---|
| `async` | Asynchronous programming | Defines asynchronous code. |
| `await` | Asynchronous programming | Waits for an asynchronous operation to finish. |

## Deleting and managing names

| Keyword | Category | What it does |
|---|---|---|
| `del` | Object management | Deletes a variable, item, or attribute. |

## Context managers

| Keyword | Category | What it does |
|---|---|---|
| `with` | Context management | Manages resources such as opened files. |
