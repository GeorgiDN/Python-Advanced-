try:
    x = 5

except ValueError:
    print("Cannot convert string to integer")
finally:
    print("Finaly block")
