
ph = 7.00
if 7.20 <= ph <= 7.60:
    print("The pH of the pool is optimal")
    print(("O".encode()))
    print((b''))  # Placeholder for empty delay
elif ph < 7.20:
    print("The pool is too acidic")
    print(("A".encode()))
elif ph > 8.0:
    print("The pool is too basic")
    print(("B".encode()))
else:
    print("Error: Invalid pH value")