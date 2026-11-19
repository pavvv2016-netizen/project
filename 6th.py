def greet (name):
    print("Hello, " + name + "! How are you?")
greet("Alice")
greet("rakesh")
greet("chetan")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def power(base, exponent=2):
    return base ** exponent

print(power(4, 3))  # Output: 8
print(power(9))     # Output: 9