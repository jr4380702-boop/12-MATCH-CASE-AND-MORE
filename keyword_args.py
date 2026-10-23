"""
In Python, keyword arguments are arguments that are preceded by an identifier (the parameter’s name) when you call a function.
They make your code easier to read and allow you to change the order of arguments when calling a function.
"""
def hello(greeting, title, first, last):
    print(greeting, title, first, last)

# call the function with positional arguements - this means the order matters:
hello("Hello", "Mr.", "Evan", "Burlingame")
# what happens if we change the order
hello("Even", "Hello", "Burlingame", "Mr." )
# try again with keyword arguements:
hello(first="Evan", greeting="Hello", last="burlingame", title="Mr.")

# Note: You can mix, but positional arguements must be first
hello("Hello", "Mr.", last="Burlingame", first="Even")
